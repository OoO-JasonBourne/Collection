# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO

# 创建Flask实例
app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/Ningbo_Project'

# 创建拓展实例插件并绑定到程序实例
db = SQLAlchemy(app)

# socketio = SocketIO(app)

# 定义模型
class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120))

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# socketio = SocketIO(app)

# 创建数据表
with app.app_context():
    db.create_all()
#
@app.route('/')
def index():
    data = MyModel.query.all()
    # return render_template('index.html', data=data)
    return data

# @app.get('/user')
# def user_list():
#     q = db.select(User).order_by(User.username)
#     users = db.session.execute(q).scalars()
#     return {
#         "message": "ok",
#         "data": [user.json() for user in users]
#     }



# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#
# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# def check_for_changes():
#     with app.app_context():
#         while True:
#             # 检测数据库变化的逻辑
#             changed_data = MyModel.query.filter_by(data='changed').all()
#             if changed_data:
#                 socketio.emit('data_changed', {'message': 'Data changed'})
#             socketio.sleep(10)  # 每10秒检测一次




if __name__ == '__main__':
    # socketio.start_background_task(check_for_changes)
    # socketio.run(app, host='127.0.0.1', port='5002', allow_unsafe_werkzeug=True)
    app.run(debug=True)     # 热更新
