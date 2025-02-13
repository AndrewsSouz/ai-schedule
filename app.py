import database_handler
from flask import Flask, request


app = Flask(__name__)


# controller
@app.route('/schedule', methods=['POST'])
def hello_name():
    data = request.json
    return database_handler.insert_user_schedule(data['schedule'])

if __name__ == '__main__':
    app.run(debug=True)
