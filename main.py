from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
con = sqlite3.connect('material.db', check_same_thread=False)
table_name = 'tsxt_name'
label = ['学号', '姓名', '性别', '年级', '取向']


@app.route('/')
def Material_Management():
    # 获取数据库material_table表的内容
    cur = con.cursor()
    sql = 'select * from {0}'.format(table_name)
    cur.execute(sql)
    content = cur.fetchall()
    # 获取数据库表的表头
    labels = [tuple_data[0] for tuple_data in cur.description]
    return render_template('test.html', content=content, labels=labels)


@app.route('/edit', methods=['get'])
def edit():
    content = [request.args.get(i) for i in label]
    print(content)
    sql = 'update {0} set {1}="{6}",{2}="{7}",{3}="{8}",{4}="{9}" where {5}="{10}"'.format(table_name,
                                                                                           label[1], label[2], label[3],
                                                                                           label[4], label[0],
                                                                                           content[1], content[2],
                                                                                           content[3], content[4],
                                                                                           content[0])
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return "数据写入成功！"


@app.route('/add', methods=['get'])
def insert():
    content = [request.args.get(i) for i in label]
    print(content)
    sql = 'insert into {0} ({1},{2},{3},{4},{5}) values("{6}","{7}","{8}","{9}","{10}")'.format(table_name, label[0],
                                                                                                label[1],
                                                                                                label[2], label[3],
                                                                                                label[4], content[0],
                                                                                                content[1], content[2],
                                                                                                content[3], content[4])
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return "数据写入成功！"


if __name__ == '__main__':
    app.run(debug=True)
