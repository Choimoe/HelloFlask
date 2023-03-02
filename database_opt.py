import sqlite3
from sqlite3 import Cursor

from flask import Flask, render_template

app = Flask(__name__)
con = sqlite3.connect('material.db')

table_name = 'tsxt_name'
label = ['学号', '姓名', '性别', '年级', '取向']
content = ['202222222202', 'wxy', '男', '2022', '卷']


def create():
    sql = 'create table {0} ({1},{2},{3},{4},{5})'.format(table_name, label[0], label[1], label[2], label[3], label[4])
    result: Cursor = con.execute(sql)
    con.commit()
    return True if result else False


def insert():
    sql = 'insert into {0} ({1},{2},{3},{4},{5}) values("{6}","{7}","{8}","{9}","{10}")'.format(table_name, label[0],
                                                                                                label[1],
                                                                                                label[2], label[3],
                                                                                                label[4], content[0],
                                                                                                content[1], content[2],
                                                                                                content[3], content[4])
    result = con.execute(sql)
    con.commit()
    return True if result else False


def query():
    sql = 'select * from {0}'.format(table_name)
    result = con.execute(sql)
    return list(result)


@app.route('/')
def hello_world():
    return render_template('test.html')


if __name__ == '__main__':
    create()
    insert()
    print(query())
