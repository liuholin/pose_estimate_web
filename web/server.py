import socket
import threading
import time
from collections import deque
import pickle


class ServerHandler:

    def __init__(self):
        self.request_data = deque()
        print(id(self.request_data))
        self.response_data = deque()

    def response(self):
        response_host = ('0.0.0.0', 10011)
        response = socket.socket()
        response.bind(response_host)
        response.listen(5)
        while 1:
            conn, addr = response.accept()
            self.response_data.clear()
            self.send_data(conn)

    def send_data(self, conn):
        while 1:
            try:
                print('read', self.response_data)
                data = self.response_data.pop()
                print('data', data)
                conn.send(data)
            except IndexError:
                time.sleep(1)
            except Exception:
                print('client closed, send_data stop')
                conn.close()
                break

    def request(self):
        request_host = ('0.0.0.0', 10010)
        request = socket.socket()
        request.bind(request_host)
        request.listen(5)
        while 1:
            conn, addr = request.accept()
            self.recv_data(conn, addr)

    def recv_data(self, conn, addr):
        while 1:
            data =conn.recv(1024)
            if not data:
                print('disconnect')
                break
            try:
                pickle_data = pickle.loads(data)
                #print(type(pickle_data))
                #print(pickle_data['Pitch'])
                self.request_data.appendleft(str(pickle_data))
            except:
                print('pickle.loads error')
                continue

        conn.close()

    def run(self):
        request_thread = threading.Thread(target=self.request)
        response_thread = threading.Thread(target=self.response)
        request_thread.start()
        response_thread.start()


socket_server = ServerHandler()
# 随web服务器一起启动， 监听10010和10011端口
# 如监听到10010端口， 则开始循环读取数据并赋值给request_data
# 如监听到10011端口， 则读取
