# manage.py

from flask_script import Manager

from my_app import app

manager = Manager(app)

app = Flask(__name__)

manager = Manager(app)


if __name__ == "__main__":
    manager.run()
