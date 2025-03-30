# CRD Website

## Installation
Create project directory and clone repository into that

Install Python 3.13

Create a virtual environment (`python -m venv venv`) with python 3.13 in your project directory

Activate your virtual envronment (`source venv/bin/activate` on Linux/MacOS `.\venv\Scripts\activate` on Windows)

Install dependencies with `pip install -r requirements.txt` from inside the cloned repository (`crd-website`)

Run `python manage.py migrate`

Run `python manage.py createsuperuser` and follow the prompts, you do not need the email address

Run `python manage.py runserver` to run the development website

Browse to `http://127.0.0.1:8000/admin` and log in with the username and password you have created in the createsuperuser step

## Development
If you want to contribute to the website, create a feature branch, commit your changes and open a pull request to main
