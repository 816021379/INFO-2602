import flask_login
from flask_login import LoginManager, current_user
from flask_jwt import JWT
from App.models import User
login_manager = LoginManager()

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


def login_user(user, remember):
    print("Logged in "+ user.username)
    return flask_login.login_user(user, remember=remember)


def logout_user():
    print("Logged out "+current_user.username)
    flask_login.logout_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)