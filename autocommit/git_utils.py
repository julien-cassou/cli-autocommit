import subprocess
import requests 
import os
from dotenv import load_dotenv

def get_git_diff() : 
    """
    Exécute la commande `git diff --staged` et récupère son résultat sous forme 
    de chaîne de caractères.
    """

    try : 
        result = subprocess.run(
            ['git', 'diff', '--staged'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e :
        print(f"Erreur lors de l'exécution de la commande git: {e.stderr}")
        return None
    except FileNotFoundError :
        print("Erreur: Git n'est pas installé ou n'est pas accessible.")
        return None

def generate_commit_message(diff_output):
    """
    Envoie le diff à l'API Mistral pour générer un message de commit.
    """
    if not diff_output:
        return None

    # URL de l'API Mistral
    mistral_url = "https://api.mistral.ai/v1/chat/completions"

    # Récupère la clé API Mistral depuis .env
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Erreur: La clé API Mistral n'est pas configurée dans le fichier .env.")
        return None

    # Prompt pour Mistral
    prompt = f"""
    Génère un message de commit conventionnel en français pour les changements suivants.
    Utilise le format suivant : type(scope): description.
    Types possibles : feat, fix, docs, style, refactor, test, chore.
    Scope : optionnel, décrit la partie du code concernée.
    Description : courte et descriptive.

    Changements :
    {diff_output}
    """

    model = os.getenv("MISTRAL_MODEL")
    if not model :
        model = "mistral-tiny"

    # Payload pour l'API Mistral
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    # Headers pour l'API Mistral
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Envoie la requête à Mistral
        response = requests.post(mistral_url, json=payload, headers=headers)
        response.raise_for_status()  # Lève une erreur si la requête échoue

        # Récupère le message de commit généré
        commit_message = response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        return commit_message
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à Mistral: {e}")
        return None