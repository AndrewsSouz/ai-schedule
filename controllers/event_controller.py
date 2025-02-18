from flask import Blueprint, request
import database_handler

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedule', methods=['GET'])
def get_schedule():
    return database_handler.get_user_schedule()

@schedule_bp.route('/schedule', methods=['POST'])
def add_schedule():
    event = request.json
    return database_handler.insert_user_schedule(event)
