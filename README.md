
# Exam Site

A project for Exam Site.



## Installation

Install project with venv

```bash
  python -m venv venv
  after zip: open project folder  SchollProject
  pip Install -r requirements.txt
  python manage.py runserver
```
# run docker compose file
docker-compose build
# use to run docker container
docker-compose up

# use this commands to run python manage.py commands
```
docker-compose run app python manage.py runserver
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py migrate
docker-compose run app python manage.py createsuperuser
```

    

