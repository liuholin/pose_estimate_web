# -*- coding:utf-8 -*-
import re

from flask import Flask, request, render_template, jsonify

from server2 import socket_server

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/', methods=['GET', 'POST'])
def api():
        try:
            data = socket_server.request_data.pop()
        except IndexError:
            data = 0
        return jsonify({'data': data})


if __name__ == '__main__':
    socket_server.run()
    app.run(host='0.0.0.0', debug=False, use_reloader=False)
