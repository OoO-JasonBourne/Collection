# -*- coding: utf-8 -*-

'''
对数据库进行增、删、改、查
'''

import requests
from faker import Faker


baseURL = 'http://127.0.0.1:5000'


faker = Faker('ZH-CN')

# 添加数据
for i in range(2):
    user = {
        'username': faker.name(),
        'email': faker.email()
    }
    # # 添加
    # with requests.post(baseURL + '/addUser', json=user) as response:
    #     print(response.json())


# # 查询
# with requests.get(baseURL + '/user') as response:
#     print(response.text)
#     # print(len(response))

# # 根据id查询数据
# with requests.get(baseURL + '/user/1') as response:
#     print(response.json())

# # 分页查询
# with requests.get(baseURL + '/userPagi?per_page=10') as response:
#     print(response.text)

# 修改数据
with requests.put(baseURL + '/changeUser/49', json=user) as response:
    print(response.text)


# # # 根据id删除数据
# with requests.delete(baseURL + '/deleteUser/6') as response:
#     print(response.text)

# 根据id删除多条数据
# with requests.delete(baseURL + '/deleteUsers/20/46') as response:
#     print(response.text)