from sqlalchemy import desc
from App.models import User
from App.database import db
import json
import random


def update_score(username):
    currentUser= User.query.filter_by(username =username).first()
    currentUser.score= currentUser.score+1
    db.session.commit()

def get_all_users():
    return User.query.all()

def checkword(input,word,username):
    if (input.lower() == word.lower()):
        update_score(username)
        return generateword()
    else:
        return "Not spelled correctly"

def get_user_profile(username):
    user = User.query.filter_by(username =username).first()
    return str(user.score)


def create_user(username, password):
    userexists = User.query.filter_by(username =username).first()
    if(userexists):
        return "User already exists"
    else:
        if(len(username)>2):
            newuser = User(username=username, password=password)
            db.session.add(newuser)
            db.session.commit()
            return("Account created!")
        else:
            return("Username must be longer than 2 characters")

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    print(users)
    return users

def get_all_users():
    return User.query.all()

def get_user_by_id(queryid):
    user=User.query.filter_by(id=queryid).first()
    return user.username

def get_leaderboard_users():
    users = User.query.order_by(desc(User.score)).all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    print(users)
    return users

def generateword():
      with open('./App/controllers/words.json') as f:
        word = json.load(f)
        wordcount = len(word)
        return word[random.randrange(0,wordcount)]
