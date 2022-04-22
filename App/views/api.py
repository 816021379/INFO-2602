from flask import Blueprint, redirect, render_template, request, send_from_directory,jsonify
from flask_login import login_required
api_views = Blueprint('api_views', __name__)
from App.controllers import (

    create_user, 
    delete_user,
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

@api_views.route('/profile', methods=['GET'])
def get_profile_page():
    return send_from_directory('static','index.html')

@api_views.route('/delete', methods=['GET'])
def get_delete_page():
    return send_from_directory('static','index.html')



