# otogipush
Shortens git add, commit, and push your local repo to github, useful if<br>
you have several github accounts and you don't want to show your personal access token<br>
on the screen if you are doing a live stream, just run this script.<br>
<br>
but if you only use one account and use SSH, don't use this script, this script is intended<br>
only for those who need it. I don't need comments/criticism if you don't have the needs according<br>
to the conditions above.

# Requirement
You must have python version 3 and above installed on your machine<br>
(Unix-like Distro only, sorry windows user, i'm not part of ur community).

## Use Alias
Add this code in your `.bashrc` file as an alias:

```bash
alias gitpush='python ~/path/to/gitpush.py'
# for the "gitpush" alias name, you can change it to any alias you like.
# for this path: ~/path/to/gitpush.py you must change it to the location,
# where do you put the gitpush.py file, don't make the wrong location.
```
After that, run in your terminal the following command:

```bash
source ~/.bashrc
```

# How To use
Now you can use the gitpush alias to run Python scripts in the following way:

```bash
gitpush "what-message for ur commit"
#Once again, the "gitpush" command depends on what alias name is set.
```
Remember, use the above code in your local repository, not outside the repository that you want to push to GitHub.
