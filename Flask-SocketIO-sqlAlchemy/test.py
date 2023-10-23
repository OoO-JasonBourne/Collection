# -*- coding: utf-8 -*-
import requests
from faker import Faker


baseURL = 'http://127.0.0.1:5002'


faker = Faker('ZH-CN')

# 添加数据
for i in range(5):
    user = {
        'username': faker.name(),
        'email': faker.email()
    }
    # with requests.post(baseURL + '/addUser', json=user) as response:
    #     print(response.json())


# 查询
with requests.get(baseURL + '/user') as response:
    print(response.json())
    # print(len(response))

# 根据id查询数据
with requests.get(baseURL + '/user/6') as response:
    print(response.json())

# 添加
# with requests.post(baseURL + 'addUser')