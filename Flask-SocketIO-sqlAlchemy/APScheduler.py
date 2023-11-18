'''
监测数据表变化
'''

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import pymysql
from flask_socketio import SocketIO, send, emit
import threading
import json

# 创建Flask实例
app = Flask(__name__)
# 创建socketIO对象,设置允许的跨域请求来源以及异步模式
socketio = SocketIO(app, cors_allowed_origins = '*')
# socketio = SocketIO(app, cors_allowed_origins = '*', async_mode = "threading")

# 连接数据库并自动提交
host = "localhost"
user = "root"
password = "root"
db_name = "Ningbo_Project"

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", database=db_name, autocommit=True)
# 接受socket信息
@socketio.on('connect')
def handle_connect():
    print('client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('client disconnected')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + json.dumps(data))

# 全局变量，用于存储上一次查询的数据
previous_data = []

# 查询数据表
def check_data_change():
    global previous_data
    # 创建游标对象
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 执行Sql查询语句
    sql = "SELECT * FROM user ORDER BY id DESC LIMIT 10"
    cursor.execute(sql)
    new_data = cursor.fetchall()
    cursor.close()
    if new_data != previous_data:
        print('数据发生改变')
        print('previous_data', previous_data)
        print('new_data', new_data)
        # 更新上一次的数据
        previous_data = new_data
        message = '数据发生变化'
        socketio.send(message)
        socketio.emit("message", {"data": 'message'})



    # return json.dumps(data, cls=ComplexEncoder)



if __name__ == '__main__':

    # 创建定时任务
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_data_change, 'interval', seconds=2)  # 每5分钟执行一次检查
    scheduler.start()
    socketio.run(app, host='127.0.0.1', port=5002, allow_unsafe_werkzeug=True)

