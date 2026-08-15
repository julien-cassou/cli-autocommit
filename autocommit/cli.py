from autocommit.git_utils import get_git_diff, generate_commit_message

def main():
    print("Récupération du git diff des fichiers staged...")
    diff_output = get_git_diff()

    if not diff_output:
        print("Aucun fichier staged ou erreur lors de la récupération du diff.")
        return

    print("\nGit diff des fichiers staged:\n")
    print(diff_output)

    print("\nGénération du message de commit avec Mistral...")
    commit_message = generate_commit_message(diff_output)

    if commit_message:
        print("\nMessage de commit généré:\n")
        print(commit_message)
    else:
        print("Erreur lors de la génération du message de commit.")

if __name__ == "__main__":
    main()