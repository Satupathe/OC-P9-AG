# OC-P9-AG
This readme focus on how to set up your computer, launch the local server and use the different website's features with the following steps:
-download elements on your computer
-set your computer on the right configuration
-launch your local server
-acces the website

This program respect PEP8 writing conventions

Be careful: - For each code line found in the README between "", take only the text and forget about ""
	    - In your powershell windows, using your right click will automatically paste
	    - In your terminal application for mac or linux use the right click and paste

PYTHON INSTALLATION:
To run this code you need Python 3.8 version or further 
Download python's executable file on the following website: "https://www.python.org/downloads/"
Lauch the installation without any modification.

CREATION OF THE WORKING REPOSITORY:
To run this code and find the informations you seek for, you need to create a working folder.
With your explorer go at the place you choose to work, create a new working folder. 

SET YOUR SYSTEM TO THE RIGHT PLACE (your working folder pathway):
You now need to open your terminal:
- windows: use Windows Powershell(admin). to find it use windows + x as keyboard shortcut 
- mac: use terminal. to find it open your Utilities folder in applications
- linux: use terminal. to find it type terminal in your applications's research bar

In the new window, you have to put your working folder's path
For that go back to your windows explorer, go in your working folder.
now you're in, copy the pathway of your folder found in the adress bar (C:\Users\...\.... for windows)

In the terminal type "cd .." several time. you need to be at the root of your computer (C: for Windows, /Home on Mac)
Next type "cd 'yourfolderpathwaythatyoujustcopied'" (this time keep the small quote marksand let a space after cd) and ENTER

CREATE A SPECIAL WORKING ENVIRONMENT:
With Python, you have to create a special working environment to install specifics modules for each project.
In the terminal using the following command will set a new environment 'env':
"python -m venv env" and ENTER

You now need to activate it, for that:
-On Windows: "source env/Scripts/activate" or env/Scripts/activate.ps1 and ENTER
-On Mac and Linux: "source env/bin/activate" and ENTER

if you have any issue to activate your environment:
-go to the env folder and search for the folder name which contain the "activate" file 
-replace "Scripts" by this name

With that your working environment is now running

DOWNLOAD REQUESTED FILES AND MODULES:
Go to the following repository: https://github.com/Satupathe/OC-P9-AG
-find the green button
-clic on the arrow
-choose download ZIP
-download the zip file
-extract its content and put it in your working folder

now use this command on the terminal:
"pip install -r requirements.txt"

This step will install necessary modules to execute the code. 
Let it work because it can take few minutes depending on your internet connection

LAUNCH THE SERVER:
In your terminal type "cd livrables"
Then type "python manage.py runserver and after a few seconds you'll see:

"System check identified no issues (0 silenced).
September 29, 2021 - 11:39:14 (with your actual date)
Django version 3.2.7, using settings 'LITReview.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK."

You have now activated your local server.

ACCESS THE WEBSITE:
To access the website go in your browser's adress bar and paste "127.0.0.1:8000/" and be sure you have launch your server before.
This adress will lead you to the login page
PLease create an account before using the website and connect to access it's features
Use "Se déconnecter" to log out

ADMINISTRATION SITE:
You can manage all data saved in the database by using the administration site
In your adress bar paste "127.0.0.1:8000/admin/" 
Log in with "admin" as username and "37476374" as password
In the administrations site you can see and change informations of:
-users
-tickets
-reviews
-follows

SHUT DOWN YOUR SERVER AND QUIT YOUR WORKING ENVIRONMENT:
To shut down your server, in the terminal use ctrl and c with your keyboard
Still in your terminal quit your working environment with deactivate
You can now quit your terminal using the closing button

Thank you for reading this README and using my program




