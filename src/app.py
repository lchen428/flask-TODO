from flask import Flask, request, jsonify, abort
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import TodoForm

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
    mytodo = service.get_by_id(id)
    if mytodo is not None:
        return jsonify(mytodo.json())
    return 'No todo list for id', 404


@app.route('/todo', methods=['POST'])
def post_todo():
    form = TodoForm.CreateTodoForm(request.form)
    if not form.validate():
        abort(400, form.errors)

    name = request.form['name']
    if service.get_by_name(name) is None:
        created_date = datetime.datetime.now()
        newtodo = Todo(None, name, False, created_date, None)
        service.add(newtodo)
        return jsonify(newtodo.json()), 201
    return "Post failed because todo name already exists", 400


@app.route('/todo/<int:id>', methods=['put'])
def put_todo_id(id):
    #name = request.form['name']
    #done = request.form['done']
    #updated_date = datetime.datetime.now()
    #mytodo = Todo(id, name, done, None, updated_date)
    todo = service.get_by_id(id)
    if not todo:
            abort(404, "Id {} doesn't exist".format(id))

    form = TodoForm.UpdateTodoForm(request.form)
    if not form.validate():
        abort(400, form.errors)

    form.populate_obj(todo)
    todo.updated_date = datetime.datetime.now()

    service.update(todo)
    return jsonify(todo.json())


@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    if service.delete(id):
        return " ", 204
    return "Delete failed because of non-exisiting todo id", 404
