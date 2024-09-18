import subprocess
import os

# Configuration - Replace with your GitHub credentials
USERNAME = "<YOUR_USERNAME>"
TOKEN = "<YOUR_PERSONAL_ACCESS_TOKEN>"
CREDENTIALS_FILE = os.path.expanduser("~/.git-credentials")

def run_command(command):
    """Execute shell command and return the output"""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print("Error message:", result.stderr.strip())
    return result

def setup_git_credentials():
    """Set up Git credentials file if not already present"""
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'w') as file:
            file.write(f"https://{USERNAME}:{TOKEN}@github.com\n")

def get_repo_url():
    """Retrieve the repository's remote URL"""
    return run_command("git config --get remote.origin.url")

def git_push(commit_message):
    """Add files, commit, and push to GitHub"""
    # Set up Git credentials
    setup_git_credentials()

    # Add files and commit
    run_command("git add .")
    commit_result = run_command(f"git commit -m \"{commit_message}\"")

    # Push to the current repository
    push_result = run_command("git push origin main")

    # Check if push was successful
    if push_result.returncode == 0:
        print(f"Successfully pushed to {USERNAME}!")
    else:
        print(f"Failed to push to {USERNAME}.")
        print("Push error message:", push_result.stderr.strip())

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gitpush.py <commit_message>")
        sys.exit(1)

    commit_message = sys.argv[1]
    git_push(commit_message)
