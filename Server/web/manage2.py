# -*- coding:utf-8 -*-
import json
import re

from flask import Flask, request, render_template, jsonify

from server import socket_server

import sqlite3

'''conn = sqlite3.connect('test.db')

print ("Opened database successfully")



#读取数据库
cursor = conn.execute("SELECT id, name from PATIENT")
tzz = []
count = 0
for row in cursor:
   pp=[str(count),str(row[0])+row[1]]
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   count=count+1
   tzz.append(pp)

tzz.append(['number',count])
tzz=dict(tzz)
print(tzz)'''

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('merge.html')


@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.form['data']
        nam=data[:-1]#最后一位是id
        idd=int(data[-1])
        print(nam,idd)
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")


        conn.execute("INSERT INTO PATIENT (ID,NAME) \
              VALUES ({},'{}')".format(int(idd),nam));
        conn.commit()

        #        cou=tzz['number']
#        del tzz['number']
#        tzz[str(count)]=nam+str(idd)
#        tzz['number']=cou+1
#        print(tzz)
        if re.match('[0-9a-fA-F]*$', data):
            socket_server.response_data.appendleft(data.encode())
            return jsonify({'result': 1})
        else:
            return jsonify({'result': 0})
    else:
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            cursor = conn.execute("SELECT id, name from PATIENT")
            tzz = []
            count = 0
            for row in cursor:
                pp = [str(count), str(row[0]) + row[1]]
                print("ID = ", row[0])
                print("NAME = ", row[1])
                count = count + 1
                tzz.append(pp)
            tzz.append(['number', count])
            tzz = dict(tzz)
            print(tzz)
            data = socket_server.request_data.pop()
            #print(123)
            # print(data)
        except IndexError:
            #data = 0
#            web_data = {'core_node_name':'104', 'node':'N0040', 'status':'0'}
#            data = str(web_data)
            data= str(tzz)
#        print( jsonify({"data":json.loads(data.replace("'", '"'))}))
        return jsonify({"data":json.loads(data.replace("'", '"'))})




@app.route('/api2/', methods=['GET', 'POST'])
def api2():
    #从删库到跑路
    if request.method == 'POST':
        data = request.form['data']
        print(data)
        iddd=int(data[-1])
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        conn.execute("DELETE from PATIENT where ID={};".format(iddd))
        conn.commit()
        if re.match('[0-9a-fA-F]*$', data):
            socket_server.response_data.appendleft(data.encode())
            return jsonify({'result': 1})
        else:
            return jsonify({'result': 0})

if __name__ == '__main__':
    socket_server.run()
    app.run(host='0.0.0.0', debug=False, use_reloader=False)
