# CSC381Project
1.	Clone github repo (“git clone https://github.com/VinnieColon/CSC381Project” in terminal)
2.	Change to wherever you saved app.py (the directory) and type “cd~/CSC381Project” in terminal.
3.	Create virtual environment with (“python3 -m venv venv” in terminal)
4.	Open virtual environment (“source venv/bin/activate” in terminal)


# Uploading to Github
1. Download Github Extensions
2. Go to source control on the left side of screen
3. Type a message about what you changed and added
4. Click "Commit and Push"


# Setting up Virtual Environment
1. Open up a new terminal and navigate to the folder for your project
2. Once there type the command "python3 -m venv venv" and wait for a moment while it creates virtual env
3. Once venv file appears in directory type the command "source venv/bin/activate" to activate virtual environment
4. To exit virtual environment press ctrl + d


# Installing Necessary Libraries
- Activate your virtual environment using method described above
- Enter the following commands into the terminal to get necessary libraries (We will add to this as we go)
    pip install pandas
    pip install numpy
    pip install flask
    pip install Flask-WTF
    pip install scipy


# How to Run App With Flask
- Running a flask app isn't as simple as just clicking the green button in the top right
- To run the app you will have to activate your virtual environment and enter the following commands into the terminal (separately)
    export FLASK_APP=data_routes
    flask run
- The terminal will print a few lines, one of them saying "* Running on http://SomeAddress" if you click this link it will bring you to the app in your browser
- To turn the app off, go to the terminal and press ctrl + c and the flask server will stop running