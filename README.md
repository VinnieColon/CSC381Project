# CSC381Project
1.	Clone github repo (“git clone https://github.com/VinnieColon/CSC381Project” in terminal)
2.	Change to wherever you saved app.py (the directory) and type “cd~/CSC381Project” in terminal.


## Uploading to Github
1. Download Github Extensions
2. Go to source control on the left side of screen
3. Type a message about what you changed and added
4. Click "Commit and Push"


## Setting up Virtual Environment
1. Open up a new terminal and navigate to the folder for your project
2. Once there type the command "python3 -m venv venv" and wait for a moment while it creates virtual env
3. Once venv file appears in directory type the command "source venv/bin/activate" to activate virtual environment
4. To exit virtual environment press ctrl + d


## Installing Necessary Libraries
- Activate your virtual environment using method described above
- Enter the following commands into the terminal to get necessary libraries (We will add to this as we go)
    - pip install pandas
    - pip install numpy
    - pip install flask
    - pip install Flask-WTF
    - pip install scipy


## How to Run App With Flask
- Running a flask app isn't as simple as just clicking the green button in the top right
- To run the app you will have to activate your virtual environment and enter the following commands into the terminal (separately)
    - export FLASK_APP=data_routes
    - flask run
- The terminal will print a few lines, one of them saying "* Running on http://SomeAddress" if you click this link it will bring you to the app in your browser
- To turn the app off, go to the terminal and press ctrl + c and the flask server will stop running


## How to Setup Git/GitHub on Command Line Terminal
- Often times it is faster/easier to use command line instead of github extensions of desktop GUI
- First, go to project folder in command line and type "git init" to initialize local repository
    - Everytime you start working on project type "git init" into command line
- Now we will connect your local git repo to the github repo we all share
    1. Go to the repository on GitHub and click the green button that says "code"
    2. In the drop-down menu that appears there will be a link, copy it
    3. Go to command line and enter the command "git remote add origin (link)" where (link) is the link you copied from previous step
- You are now connected to the remote github repo which we named "origin", if you ever want to see the list of remote repos you are connected to enter "git remote -v"
- To get the data from this remote repo into your local one enter "git pull origin main"
    - This command can be used whenever you want to get the most updated version of the project


## 
