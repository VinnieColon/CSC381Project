# CSC381Project
1.	Clone github repo (“git clone https://github.com/VinnieColon/CSC381Project” in terminal)
2.	Change to wherever you saved app.py (the directory) and type “cd~/CSC381Project” in terminal.
<br>

## Setting up Virtual Environment (For Mac)
1. Open up a new terminal and navigate to the folder for your project
2. Once there type the command `python3 -m venv venv` and wait for a moment while it creates virtual env
3. Once venv file appears in directory type the command `source venv/bin/activate` to activate virtual environment
4. To exit virtual environment press ctrl + d
<br>

## Installing Necessary Libraries
- Activate your virtual environment using method described above
- Enter the following commands into the terminal to get necessary libraries (We will add to this as we go)
    - `pip install pandas`
    - `pip install numpy`
    - `pip install scikit-learn`
    - `pip install matplotlib`
    - `pip install streamlit`
<br>

## Running the app
- Once you have activated your virtual environment and downloaded all necessary libraries you can run the app with the command `streamlit run Upload_CSV.py` in the terminal
