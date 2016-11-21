from flask import Flask, request, jsonify, abort
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import form

app = Flask(__name__)
@app.errorhandler(400)
def error(error):
    print vars(error)
    err = {'message': error.description}
    return jsonify(**err), 400

app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from model import Todo  # noqa: E402
from service import Service  # noqa: E402

service = Service()


@app.route('/todo')
def get_todo():
    return jsonify([todo.json() for todo in service.get_all()])


@app.route('/todo/<int:id>')
def get_todo_id(id):
    todo = service.get_by_id(id)
    if not todo:
        abort(404, "Id {} doesn't exist".format(id))

    return jsonify(todo.json())


@app.route('/todo', methods=['POST'])
def post_todo():
    myform = form.CreateTodoForm(request.form)
    if not myform.validate():
        abort(400, myform.errors)

    name = request.form['name']
    if service.get_by_name(name) is None:
        created_date = datetime.datetime.now()
        newtodo = Todo(None, name, False, created_date, None)
        service.add(newtodo)
        return jsonify(newtodo.json()), 201
    return "Post failed because todo name already exists", 400


@app.route('/todo/<int:id>', methods=['put'])
def put_todo_id(id):
    todo = service.get_by_id(id)
    if not todo:
            abort(404, "Id {} doesn't exist".format(id))

    myform = form.UpdateTodoForm(request.form)
    if not myform.validate():
        abort(400, myform.errors)

    myform.populate_obj(todo)
    todo.updated_date = datetime.datetime.now()

    service.update(todo)
    return jsonify(todo.json())


@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = service.get_by_id(id)
    if not todo:
        abort(404, "Id {} doesn't exist".format(id))

    service.delete(todo)
    return " ", 204
