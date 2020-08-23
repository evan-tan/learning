# Initializing a new git repo from CLI
If folder isn't created, first create it, inside that folder...
```bash
touch README.md
git init
git add -A
git commit -m "Initial commit"
# If git repo has not been created via github.com, https://github.com/new
git remote add origin git@github.com:user_name/repo_name.git
git push -u origin master
```

# Working with branches
Changes to code should be done in branches with an appropriate name.
## Branch naming examples
- feature/my_cool_feature
- bugfix/fixing_some_error
- refactor/use_msft_cpp_style_guide


```bash
cd repo_name
git branch branch_name
# After making changes to file1.cpp file2.cpp
git add file1.cpp file2.cpp
git commit -m "Implemented part of feature"
git push --set-upstream origin branch_name
```
# Merge conflicts during git pull
```bash
# Stash your local changes
git stash
# Update local repo
git pull
# Apply changes and solve merge conflicts manually
git stash pop
```


# To see latest commit in your repo
```bash
git log --name-status HEAD^..HEAD
git show --summary
git show --summary --name-only

# With commit ID, Author name, Date/time, and commit message
git log -1 --stat
```

# Some common git aliases
These let you use `co`, `br`, `ci`, `st` instead having to type out full words all the time.
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```