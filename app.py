from flask import Flask
from controllers.schedule_controller import schedule_bp


app = Flask(__name__)
app.register_blueprint(schedule_bp)

if __name__ == '__main__':
    app.run(debug=True)
