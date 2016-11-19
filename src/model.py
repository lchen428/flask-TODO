from src.app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    done = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)

    def __init__(self, id, name, done, created_date, updated_date):
        self.id = id
        self.name = name
        self.done = done
        self.created_date = created_date
        self.updated_date = updated_date

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'done': self.done,
            'created_date': self.created_date,
            'updated_date': self.updated_date
        }
