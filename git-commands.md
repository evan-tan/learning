# Initializing a new git repo from CLI
If folder isn't created, first create it, then inside that folder...

```bash
touch README.md
git init
# Stage all files
git add -A
git commit -m "Initial commit"
# If git repo has not been created via github.com, do so here https://github.com/new
# Add remote using SSH
git remote add origin git@github.com:user_name/repo_name.git
git push -u origin master
```



# Working with branches
Changes to code should be done in branches with an appropriate name.

## Branch naming examples
- feature/my_cool_feature
- bugfix/fixing_some_error
- refactor/use_msft_cpp_style_guide

## Checking out a new branch
```bash
cd repo_name
git branch branch_name
# After making changes to file1.cpp file2.cpp
git add file1.cpp file2.cpp
git commit -m "Implemented part of feature"
git push --set-upstream origin branch_name
```

## Deleting a branch
```bash
# Make sure you're not currently on the branch
git checkout master
# Delete specified branch locally
git branch -d branch_name

# Delete specified branch remotely
git push origin --delete branch_name
# This would also work
git push origin :branch_name

# Prune/Remove any remote-tracking branches which no longer exist on the remote.
git fetch -p
```



# Merge conflicts
By default Git's merge tool will create BACKUP, BASE, LOCAL REMOTE files, we can prevent this by setting up the mergetool
```bash
git config --global mergetool.keepBackup false
```

## Conflicts during git pull
Note that you should be on the same branch when running `git stash pop` or shit hits the fan
```bash
# Stash your local changes
git stash
git pull
# Apply changes and solve merge conflicts manually
git stash pop
```

## Conflicts specifically for Jupyter notebook
```bash
git mergetool --tool=nbdime
nbdime config-git --enable --global
```



# Update your forked repo with commits from the original repo
```bash
# Check that repo has an upstream remote
git remote -v
# If no upstream remote, configure your repo
git remote add upstream repo_name.git
# Verify that upstream remote added
git remote -v

git pull upstream branch_name
git push origin branch_name
```



# Reverting changes...
## To a certain commit
```bash
git revert commit_id
git push
```

## For a certain file
```bash
git checkout -- file_name
```



# Logging

## Viewing latest commits
```bash
git show --summary
# With commit id, author name, date/time, and insertions/deletions
# For previous n commits
git log -n --stat
# Show short hash and commit messages
git log --oneline --decorate
# Pretty format strings
git log --pretty="-- %s"
```

## Changelogs
```bash

```



# Writing detailed commit messages
```bash
git commit -m "title" -m "description"
```



# Some common git aliases
These let you use `co`, `br`, `ci`, `st` instead having to type out full words all the time.
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```