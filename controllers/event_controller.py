from flask import Blueprint, request

import database_handler

schedule_bp = Blueprint('schedule', __name__)


@schedule_bp.route('/event', methods=['GET'])
def get_schedule():
    return database_handler.get_user_schedule()


@schedule_bp.route('/event', methods=['POST'])
def add_schedule():
    event = request.json
    return database_handler.insert_user_schedule(event)


@schedule_bp.route('/event', methods=['PUT'])
def update_schedule():
    event = request.json
    return database_handler.update_user_schedule(event)
