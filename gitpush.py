import subprocess
import sys

# Configuration
USERNAME = "ur_username"
TOKEN = "personal_access_token"

def run_command(command):
    """Executes shell commands and prints the output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(result.returncode)

def main(commit_message):
    # Make sure it is in the Git repository
    try:
        run_command("git rev-parse --is-inside-work-tree")
    except SystemExit:
        print("Error: Not a git repository (or any of the parent directories): .git")
        sys.exit(1)

    # Setting up a remote URL with a token
    try:
        result = subprocess.run("git remote get-url origin", shell=True, text=True, capture_output=True)
        remote_url = result.stdout.strip()
    except SystemExit:
        print("Error: Could not get remote URL.")
        sys.exit(1)

    https_url = f"https://{USERNAME}:{TOKEN}@{remote_url.replace('https://', '')}"
    run_command(f"git remote set-url origin {https_url}")

    # Add files, commit, and push
    run_command("git add .")
    run_command(f"git commit -m \"{commit_message}\"")
    run_command("git push origin main")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gitpush.py \"Commit message\"")
        sys.exit(1)
    commit_message = sys.argv[1]
    main(commit_message)
