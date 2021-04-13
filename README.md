# mana-classification-tool
First mana-vox Github repository - for sentence classification

To create commits in this repository, please follow the recommendations from [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).


```
npm install -g @vue/cli
npm install -s bootstrap-vue bootstrap 
cd classification-app
vue add bootstrap-vue
vue add router
```

In the folder ```classification_tool```, execute 
```
npm install
npm run serve
```
and access the app on [http://localhost:8080/](http://localhost:8080/). 


To run it:
- Go into the api folder
- Create a virtual environment with Python 3 `virtualenv -p python3 venv` (to do just once)
- Activate the virtual environment `source venv/bin/activate`
- Install the libraries with `pip install -r requirements.txt`
- Go into the src folder
- Run `python manage.py migrate` (it will create a db.sqlite3 file automatically and create all the tables that are specified thanks to the files in the folders /migrations in each app)
- To create a super user (so that you can connect to Django admin), run `python manage.py createsuperuser`
- To launch the app, run `python manage.py runserver`
- To get access to Django admin, go to http://127.0.0.1:8000/admin in your browser


Run `python manage.py test` to make run all the tests in the tests.py files.

Run `flake8` to make sure your code complies with the most known Python conventions. 
