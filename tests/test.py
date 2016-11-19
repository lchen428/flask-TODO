import os
import unittest
import src.app
from src.model import Todo
import datetime


class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        src.app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'\
            + os.path.join(src.app.app.config['BASE_DIR'], 'db.test.sqlite')
        self.test_app = src.app.app.test_client()
        src.app.db.create_all()
        todo_test = Todo(1, "cook", 0, datetime.datetime.now(), None)
        src.app.db.session.add(todo_test)
        src.app.db.session.commit()

    def tearDown(self):
        os.unlink(os.path.join(
            src.app.app.config['BASE_DIR'], 'db.test.sqlite'
        ))

    def test_get_all_todo_ok(self):
        rv = self.test_app.get('/todo')
        assert rv.status_code == 200

    def test_get_todo_ok(self):
        rv = self.test_app.get('/todo/1')
        assert rv.status_code == 200

    def test_get_todo_ko(self):
        rv = self.test_app.get('/todo/10')
        assert rv.status_code == 404

    def test_put_todo_ok_truedone(self):
        rv = self.test_app.put(
            '/todo/1',
            data=dict(name="clean", done="true")
        )
        assert rv.status_code == 200

    def test_put_todo_ok_falsedone(self):
        rv = self.test_app.put(
            '/todo/1',
            data=dict(name="clean", done="false")
        )
        assert rv.status_code == 200

    def test_put_todo_ko_emptyname(self):
        rv = self.test_app.put(
            '/todo/1',
            data=dict(name="", done="true")
        )
        assert rv.status_code == 400

    def test_put_todo_ko_emptydone(self):
        rv = self.test_app.put(
            '/todo/1',
            data=dict(name="clean", done="")
        )
        assert rv.status_code == 400

    def test_put_todo_ko_nonkey(self):
        rv = self.test_app.put(
            '/todo/10',
            data=dict(name="clean", done="true")
        )
        assert rv.status_code == 404

    def test_post_todo_ok(self):
        rv = self.test_app.post('/todo', data=dict(name="play"))
        assert rv.status_code == 201

    def test_post_todo_ko_samename(self):
        rv = self.test_app.post('/todo', data=dict(name="cook"))
        assert rv.status_code == 400

    def test_post_todo_ko_noname(self):
        rv = self.test_app.post('/todo', data=dict(name=""))
        assert rv.status_code == 400

    def test_delete_todo_ok(self):
        rv = self.test_app.delete('/todo/1')
        assert rv.status_code == 204

    def test_delete_todo_ko(self):
        rv = self.test_app.delete('/todo/10')
        assert rv.status_code == 404
