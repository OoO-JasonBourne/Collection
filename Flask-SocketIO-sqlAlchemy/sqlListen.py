from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# # from flask_socketio import SocketIO, send, emit
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/Ningbo_Project'
db.init_app(app)
# socketio = SocketIO(app)
