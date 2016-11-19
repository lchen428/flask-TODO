# flask-TODO
This small project uses flask framework & sliqte database to manage a TODO list by sending HTTP resquest.

## Get Started
### clone the project
git clone git@github.com:lchen428/flask-TODO.git

### Prepare environment
pip install virtualenv
virtualenv env
source env/bin/activate
pip install Flask
pip install -r requirement.txt

### Run test with code coverage
nosetests --with-coverage --cover-erase --cover-package=src --cover-html

### Examples
#### Lauch the server
python manager.py runserver

#### Sending HTTP request
##### Get all TODO list
curl 127.0.0.1:5000/todo
###### Get a TODO task based on id
curl 127.0.0.1:5000/todo/{id}
##### Update a TODO task based on id
curl -X PUT 127.0.0.1:5000/todo/{id} --data "name=???&done=???"
##### Create a new TODO task
curl -X POST 127.0.0.1:5000/todo --data "name=???&done=???"
##### Delete a TODO task based on id
curl -X DELETE 127.0.0.1:5000/todo/{id}
