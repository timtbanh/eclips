# Eclips

## Installation:
  Make sure you have Python (2.7.13 preferred) and pip installed
    Download link here: https://www.python.org/downloads/
    Help for Windows: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation
  Clone the following git repository to your local directory:
  ```
  git clone https://github.com/banhfire/eclips.git
  ```
  Go to your directory where you cloned the git repo
  ```
  cd eclips
  ```
  Install the requirements
  ```
  pip install -r requirements.txt.
  ```
  Migrate the django model schema
  ```
  python manage.py migrate
  ```
  Now run the server
  ```
  python manage.py runserver
  ```
To view site enter the following website url into your browser to go to our landing page:
http://127.0.0.1:8000/

## Note:
  If you wish to view the database through the django admin site
  to see the data saved to the db.sqlite3 file

  Run the following command to create an admin on the server
  ```
  python manage.py createsuperuser
  ```
  Follow the instructions on the command line

  Go to http://127.0.0.1:8000/admin and re-enter the username and password
