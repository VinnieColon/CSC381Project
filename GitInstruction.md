# Git Instructions
This file will contain detailed instructions on how to use git and github from the command line
<br><br>

## How to Setup Git/GitHub on Command Line Terminal
- Often times it is faster/easier to use command line instead of github extensions of desktop GUI
- First, go to project folder in command line and type `git init` to initialize local repository
    - **NOTE:** Everytime you start working on project type `git init` into command line
- Now we will connect your local git repo to the github repo we all share
    1. Go to the repository on GitHub and click the green button that says "code"
    2. In the drop-down menu that appears there will be a link, copy it
    3. Go to command line and enter the command `git remote add origin (link)` where `(link)` is the link you copied from previous step
- You are now connected to the remote github repo which we named `origin`, if you ever want to see the list of remote repos you are connected to enter `git remote -v`
- To get the data from this remote repo into your local one enter `git pull origin main`
    - This command can be used whenever you want to get the most updated version of the project
<br>

## Git/GitHub Command Line: add, commit, push
- When you do tasks we generally will break them down into subtasks, each time you write code that solves a specific subproblem you will want to add and commit the changes to the repository
- To do this, do the following...
    1. Enter `git add (files)` where `(files)` are the files that you modified when writing your code each one separated by a space (Ex. git add ex1.py ex2.py)
    2. Enter `git commit -m (Message)` where `(Message)` is a small sentence about what the commit represents, make sure the message is in parentheses (Ex. `git commit -m "This is an example"`)
- Once you have completed all of the subtasks and the task is complete, we will want to push these changes to the main repo with `git push origin main`
<br>

## Git/Github Command Line: Branching and Merging
- Instead of pushing straight to main branch as we did above, we will often be pushing to a branch dedicated to a specific task being worked on
- A branch starts as a copy of the main branch (or some other but our project isn't that complex)
- To create a new branch in the remote repo, go to GitHub and click where it says "main" in top left, a menu will drop down with an option to create a new branch
- Now in your local repo in your command line type `git checkout -b (branch)` where `(branch)` is the name of the branch you used in previous step
    - This command will also switch you from the main branch to this new branch
    - This means any commits will now be on new branch instead of main
- Push and Pull commands are the same except instead of "main" use the name of new branch
- Once the task that branch is dedicated has been completed then it is ready to be merged 
    - Go to GitHub and go to your branch, click create pull request and optionally leave a little note about the branch
    - GitHub will check if there is any conflicts if there were to be a merge, make sure it says there are no conflicts
    - Go to your command line and enter `git checkout main`
    - Then enter `git merge (branch)`
    - Finally enter `git push -u origin main` to push merge to remote repo
- Delete the merged branch with `git branch --delete (branch)`