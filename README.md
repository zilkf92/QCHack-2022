# Quantum Prisoner's Dilemma

This is our implementation of the Quantum Prisoner's Dilemma.

# How to run

To run this project you have to start both the django backend as well as the gatsby frontend. Please run the django backend on localhost:8080.
Sadly we didn't find the time to host the project.

If one is unfamiliar with how django and gatsby work for Django you have to:

- Create a venv (python -m venv [yourVenvName])
- Activate the venv (On Windows ./[yourVenvName]/Scripts/activate)
- Install the requirements (pip install -r requirements.txt)
- Migrate the database (python manage.py migrate)
- And start the project (python manage.py runserver 127.0.0.1:8080)

For Gatsby:

- npm i
- npm run develop
