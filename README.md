# otogipy | 音葵py

Shortens the process of adding, committing, and pushing changes from your local repo to GitHub<br>
in just one command. This is an alternative way if you don't want to use SSH and prefer not to type many commands.

# Requirement
You must have python3 installed on your machine, better using latest version.<br>
*configuration below* is only for unix-like, I'm sorry windows users,<br>
i'm not part of ur community.

# Must Change First
## Configuration:

In `gitpush.py` file:

Replace `<YOUR_USERNAME>` with your GitHub username.<br>
Replace `<YOUR_PERSONAL_ACCESS_TOKEN>` with your GitHub personal access token.<br>

## Use Alias
Add this code in your `.bashrc` or `.zshrc` file on ur computer as an alias:

```bash
alias gitpush='python ~/path/to/gitpush.py'
# For the "gitpush" alias name, you can change it to any alias you prefer.
# For the path ~/path/to/gitpush.py, make sure to update it to the actual location
# where you have placed the gitpush.py file. Ensure that you provide the correct path.
```
After that, run in your terminal the following command:

```bash
source ~/.bashrc
```

# How To use
Now you can use the gitpush alias to run elixir scripts in the following way:

```bash
gitpush "what-message for ur commit"
# The "gitpush" command depends on the alias name you have set.
```

> Please always remember to ensure you're working within the repository you
> want to push to GitHub.

---

Using [MIT LICENSE](/LICENSE)
