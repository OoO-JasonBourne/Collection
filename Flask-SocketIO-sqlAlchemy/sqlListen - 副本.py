# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
import requests
# 创建Flask实例
app = Flask(__name__)

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/Ningbo_Project'

# 创建拓展实例插件并绑定到程序实例
db = SQLAlchemy(app)

# 定义模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120))

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


# # 创建数据表
# with app.app_context():
#     db.create_all()

# 查询数据
@app.get('/user')
def user_list():
    q = db.select(User).order_by(User.username)
    users = db.session.execute(q).scalars()
    return {"message": "ok", "data": [user.json() for user in users]}

# 根据id查询数据
@app.get("/user/<int:uid>")
def user_id(uid):
    user = db.get_or_404(User, uid)
    return {"message": "ok", "data": user.json()}

@app.route('/')
def index():
    data = User.query.all()
    # return render_template('index.html', data=data)
    return data

@app.post('/addUser')
def create_user():
    data = request.get_json()
    user = User(username = data.get('username'), email = data.get('email'))
    db.session.add(user)
    db.session.commit()
    return {"message": "ok", "data": user.json()}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5002', debug=True)     # 热更新
