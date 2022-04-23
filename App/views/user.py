from App.controllers.auth import authenticate, identity, logout_user
from flask_sqlalchemy import SQLAlchemy
from App.controllers.user import get_score, get_user_profile
from flask_login import login_required,current_user
from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect
from flask_jwt import jwt_required,current_identity
from datetime import datetime,timedelta
import jwt
from App.models.user import User
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
db = SQLAlchemy()



from App.controllers import (
    authenticate,
    identity,
    create_user, 
    delete_user,
    get_all_users,
    get_leaderboard_users,
    get_all_users_json,
    update_score,
    generateword,
    logout_user,
    login_user,
    get_user_by_id,
    checkword,
    get_user_profile
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')



@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return jsonify(users)





@user_views.route('/users/leaderboard', methods=['GET'])
def get_leaderboard():
    users= get_leaderboard_users()
    return jsonify(users)
    

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route("/api/newword",methods=['POST'])
def generate():
    wordDifficulty = request.json['difficulty']
    newword=generateword(wordDifficulty)
    return newword
    

@user_views.route("/api/increase", methods=['POST'])
@login_required
def update():
    input = request.json['input']
    print(input+" input")
    word = request.json['word']
    print(word+" word")
    difficulty = request.json['difficulty']
    print(current_user.username+" username")
    return checkword(input,word,current_user.username,difficulty)

@user_views.route('/login', methods=['POST'])
def login():
    if(request.method == 'GET'):
        return redirect('localhost:3000/login')
    if(request.method == 'POST'):
        username= request.json['username']
        password = request.json['password']
        print(request.data)
        user = authenticate(username,password)
        print(user)
        if(user):
            login_user(user,True)
            return current_user.username
        else:
            return "Invalid username or password"

@user_views.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        return "Logged out."
    else:
        return "You are not logged in."


@user_views.route("/whoami", methods=['GET'])
@login_required
def whoisit():
	return current_user.username

@user_views.route('/signup', methods=['POST'])
def signup():
	if(request.method == 'POST'):
            
            username = request.json['username']
            print(username)
            password = request.json['password']
            return create_user(username,password)

@user_views.route('/userprofile', methods=['POST'])
def get_profile():
    username =request.json['username']
    return get_user_profile(username)

@user_views.route('/getscore',methods=['POST'])
def get_user_score():
    username=request.json['username']
    return get_score(username)

@user_views.route('/deleteuser',methods=['DELETE'])
@login_required
def delete_user_account():
    username= request.json["username"]
    print(username)
    password=request.json['password']
    return delete_user(username,password)

