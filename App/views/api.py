from flask import Blueprint, redirect, render_template, request, send_from_directory,jsonify
api_views = Blueprint('api_views', __name__)
from App.controllers import (

    create_user, 
    get_all_users,
    get_all_users_json,
    update_score,
    generateword,
    logout_user,
    login_user,
)
@api_views.route('/', methods=['GET'])
def get_landing():
    return send_from_directory('static','index.html')
@api_views.route('/home', methods=['GET'])
def get_home_page():
    return send_from_directory('static','index.html')
    
@api_views.route('/marathon', methods=['GET'])
def get_marathon():
    return send_from_directory('static','index.html')
    
@api_views.route('/login', methods=['GET'])
def get_login_page():
    return send_from_directory('static','index.html')
    
@api_views.route('/leaderboard', methods=['GET'])
def get_leaderboard_page():
    return send_from_directory('static','index.html')



@api_views.route('/register', methods=['GET'])
def register_user():
    username=request.json["username"]
    password=request.json["password"]
    user_exists = User.query.filter_by(username=username).first() is not None

    if user_exists:
        abort(409)
    new_user=User(username=username)
    return jsonify(response_body),200