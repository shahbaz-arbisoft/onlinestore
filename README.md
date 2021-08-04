# onlinestore

- Make sure you have already installed python3.6.9+
- Clone the project by this URL `https://github.com/shbz44/onlinestore.git`
- Go to the project directory
- Acticvate virtual environment by running this command `source storevenv/bin/activate`
- Now install dependencies, for this run this command pip3 install -r requirements.txt
- Run the migration command `python3 manage.py migrate`
- As postgres database is used in this project, make sure to have it in your system.
- Create a superuser to use the functionality by this command `python3 manage.py createsuperuser`
- If the existing database is accesible then below two different users with different administrative roles.
    1. username: `shbz`   password: `1234`  (User for all available pages)
    2. username: `abc`   password: `Pass1234!!` (User for products only)

