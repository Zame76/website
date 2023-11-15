This project will start flask framework website development site.

NOTE: this uses pipenv virtual environment, run
    pipenv install 
at root directory to install virtual environment with needed packages.

Needed packages are:
    - flask
    - requests
    - pillow

NOTE: You will need to create 
    config.py 
file to root directory and set variable digitraffic_user = "<insert username here>".
Replace <insert username here> with your username.

To run this website, use command
    py app.py

NOTE: Do NOT use this in production environment, it is not safe! This is intended
for development use only. Search more information:
    flask production environment

There are a lot of comments in the code files, that explain the scripts better. Please
read more from there.

Files in this project:
.gitattributes
.gitignore
    - git configuration files
app.py
    - flask web server, use http://localhost:5000 address in browser when this is running 
config.py
    - you need to create this file, contains digitraffic_user information
photo.py
    - converts traffic cam photo to base64 encoded string and reduces the image size
Pipfile
Pipfile.lock
    - pipenv virtual environment setup files
README.txr
    - this file
sql.py
    - sql commands as functions
    - NOTE! at this point, there is no automatic database cleanup happening, feature is 
      coming soon. 
weather_api.py
    - calls api and return fetched information for the website, if less than 5 minutes 
      has passed, use information from database instead. This is to prevent too many
      api calls to Digitraffic
static/db/db-folder.txt
    - placeholder file, that forces creating db folder. Db folder will hold website.db
      file
static/db/website.db
    - this file will be created at first run, holds sqlite3 sql database
static/images/
    - holds image-files used by website
static/styles/default.css
    - css stylesheet file to be used by website
templates/index.html
    - contains root webpage
templates/layout.html
    - contains layout template that other html pages implement
templates/photo.html
    - shows the traffic cam photo for testing purposes
