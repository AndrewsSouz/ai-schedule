from flask import Flask, request
import database_handler


app = Flask(__name__)


# controller

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/schedule', methods=['POST'])
def hello_name():
    data = request.json
    schedule = {
        "user_id": data["user_id"],
        "schedule": data["schedule"]
    }
    print(schedule)
    return database_handler.insert_user_schedule(schedule)




if __name__ == '__main__':
    app.run()
