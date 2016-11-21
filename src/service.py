from src.app import db
from src.model import Todo


class Service:
    def get_all(self):
        return Todo.query.all()

    def get_by_id(self, id):
        return Todo.query.filter_by(id=id).first()

    def get_by_name(self, name):
        return Todo.query.filter_by(name=name).first()

    def add(self, todo):
        db.session.add(todo)
        db.session.commit()

    def update(self, todo):
        db.session.add(todo)
        db.session.commit()

    def delete(self, todo):
        db.session.delete(todo)
        db.session.commit
