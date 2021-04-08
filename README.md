# mana-classification-tool
First mana-vox Github repository - for sentence classification

To create commits in this repository, please follow the recommendations from [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).


## api
The api folder contains a Django API.


To run it:
- Go into the api folder
- Create a virtual environment with Python 3 `virtualenv -p python3 venv`
- Install the libraries with `pip install -r requirements.txt`
- Go into the src folder
- Put the db.sqlite3 file in the src folder
- To create a super user (so that you can connect to Django admin), run `python manage.py createsuperuser`
- To launch the app, run `python manage.py runserver`
- To get access to Django admin, go to http://127.0.0.1:8000/admin in your browser


Run `flake8` to make sure your code complies with the most known Python conventions.
