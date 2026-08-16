# Autocommit avec Mistral

Un outil CLI pour générer automatiquement des messages de commit conventionnels en utilisant l'API Mistral.

## Fonctionnalités

- Récupère le `git diff` des fichiers staged.
- Génère un message de commit conventionnel en français.
- Utilise l'API Mistral pour la génération de texte.

## Prérequis

- Python 3.14 ou supérieur
- Git installé et configuré
- Une clé API Mistral (disponible sur [Mistral AI](https://mistral.ai/))
- pipx (recommandé pour une installation globale sécurisée)

## Installation

1. Clone le dépôt :
```bash
git clone https://github.com/julien-cassou/cli-autocommit.git
cd cli-autocommit
```

2. Installe le package :
```bash
pipx install .
```

3. Configure ta clé API en l'ajoutant aux variables de ton environnement système. Ouvre ton fichier de profil shell (par exemple ~/.bashrc ou ~/.zshrc) et ajoutes-y cette ligne : 
```bash
export MISTRAL_API_KEY=ta_clé_api
```
Recharge ensuite ton terminal pour appliquer les changements : 
```bash
source ~/.bashrc
```

## Utilisation

Une fois installé, l'outil est accessible de n'importe où.

```bash
# Dans ton projet
git add .
autocommit
```

## Exemple de sortie

```bash
Récupération du git diff des fichiers staged...

Génération du message de commit avec Mistral...

Message de commit généré:

fix: corrige le contenu du fichier file.txt
```

## Configuration

Tu peux personnaliser le comportement du script en modifiant les variables d'environnement dans le fichier `.env` :
- `MISTRAL_API_KEY` : Ta clé API Mistral.
- `MISTRAL_MODEL` : Le modèle Mistral à utiliser (par défaut : `mistral-tiny`).

## Ce que j'ai appris

Ce projet a été une excellente opportunité pour apprendre et pratiquer plusieurs concepts en Python et en développement logiciel :

- **Manipulation de commandes système** : Utilisation de `subprocess` pour exécuter des commandes Git.
- **Gestion des variables d'environnement** : Utilisation de `python-dotenv` pour charger des configurations depuis un fichier `.env`.
- **Requêtes HTTP** : Utilisation de `requests` pour interagir avec l'API Mistral.
- **Tests unitaires** : Utilisation de `pytest` et des mocks pour tester le code.
- **Gestion des erreurs** : Comment gérer les exceptions et les erreurs dans un script Python.
- **Structure de projet** : Organisation d'un projet Python avec des modules et des packages.

Ce projet est mon premier outil CLI en Python, et j'ai beaucoup appris en le développant. J'espère qu'il sera utile à d'autres débutants comme moi !

## Tests

Pour exécuter les tests, utilise la commande suivante :
```bash
pytest tests/
```


## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.j