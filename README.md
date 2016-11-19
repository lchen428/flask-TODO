# flask-TODO
This small project uses flask framework & sliqte database to manage a TODO list by sending HTTP request. And it has been tested with 100% code coverage.

## Get Started

### Prepare environment
```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install Flask
pip install -r requirements.txt
```

### Run tests
`nosetests --with-coverage --cover-erase --cover-package=src --cover-html`

### Code convention check
```
cd "folder name"
flake8
```

### Examples
#### Launch the server
`python manager.py runserver`

#### Send HTTP request
##### Get all TODO list
`curl 127.0.0.1:5000/todo`
##### Get a TODO task based on id
`curl 127.0.0.1:5000/todo/{id}`
##### Update a TODO task based on id
`curl -X PUT 127.0.0.1:5000/todo/{id} --data "name=???&done=???"`
##### Create a new TODO task
`curl -X POST 127.0.0.1:5000/todo --data "name=???&done=???"`
##### Delete a TODO task based on id
`curl -X DELETE 127.0.0.1:5000/todo/{id}`
