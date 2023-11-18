# -*- coding: utf-8 -*-

import asyncio
import requests
import threading

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAABBBCCC'
socketio = SocketIO(app, cors_allowed_origins = '*', async_mode = "threading")

@socketio.on('connect')
def handle_connect():
    print('client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('client disconnected')

@socketio.on('message')
def handle_message(data):
    print(data)
    print('received message: ' + str(data))

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@app.route("/shutdown", methods = ['GET'])
def shutdown():
    socketio.stop()
    return "Shutting down..."

def main():
    print('running...')
    print('我在学习')
    thread_wss = threading.Thread(target = socketio.run , kwargs = {
        "app": app,
        "host": '127.0.0.1',
        "port": 5002,
        "allow_unsafe_werkzeug": True
    })
    thread_wss.start()

    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            line = 'exit'
        if not line or len(line) == 0: continue
        elif line == 'exit' or line == 'quit':
            print('exiting...')
            try:
                requests.get("http://localhost:9999/shutdown")
            except:
                pass
            thread_wss.join()
            break
        socketio.send(line)
        socketio.emit("json", { "data": line })
    print('done')

if __name__ == '__main__':
    main()
