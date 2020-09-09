#!/usr/bin/python3
# coding=utf-8

import time
import pymysql
import json

route_list = []

def route(path):
    def decorator(func):
        route_list.append((path, func))

        def inner():
            return func()
        return inner
    return decorator

@route("/index.html")
def index():
    status = "200 OK";

    response_header = [("Server", "PWS2.0")]

    with open("template/index.html", "r") as file:
        file_data = file.read()


    conn = pymysql.connect(host = "localhost",
                          port = 3306,
                          user = "root",
                          password = "123456",
                          database = "stock_db",
                          charset = 'utf8')
    cursor = conn.cursor()
    sql = "select * from info"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    data = ""
    for row in result:
        data += """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type="button" value = "添加" id = "toAdd" name = "toAdd" systemidvalue = "000007"></td>
        </tr>
        """ % row

    result = file_data.replace("{%content%}", data)
    return status, response_header, result

@route("/center.html")
def center():
    status = "200 OK"
    response_header = [("Server", "PWS2.0")]

    with open("template/center.html", "r") as file:
        file_data = file.read()

    
    data = time.ctime()
    result = file_data.replace("{%content%}", data)

    return status, response_header, result


@route("/center_data.thml")
def center_data():
    status = "200 OK"

    response_header = [("Server", "PWS2.0"), ("Connect-Type", "text/html;charset = utf-8")]
    conn = pymysql.connect(host = 'localhost',
                          port = 3306,
                          user = 'root',
                          password = '123456',
                          database = 'stock_db',
                          charset = 'utf8')
    cursor = conn.cursor()
    sql = '''select i.code, i.short, i.chg, i.turnover, i.price, i.highs,f.note_info
    from info as i inner join focus as f on i.id = f.info_id;'''

    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    center_data_list = list()

    for row in result:
        center_dict = dict()
        center_dict["code"] = row[0]
        center_dict["short"] = row[1]
        center_dict["chg"] = row[2]
        center_dict["turnover"] = row[3]
        center_dict["price"] = str(row[4])
        center_dict["highs"] = str(row[5])
        center_dict["note_info"] = row[6]
        center_data_list.append(center_dict)

    json_str = json.dump(center_data_list, ensure_acsii = False)
    print(json_str)
    return status, response_header, json_str




def not_found():
    status = "404 Not Found";
    response_header = [("Server", "PWS2.0")]
    data = "not_found"

    return status, response_header, data

def handle_request(env):
    request_path = env["request_path"]
    print("接收到的动态资源请求：", request_path)

    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        result = not_found()
        return result

    #if request_path == "/index.html":
    #    result = index()
    #    return result
    #elif request_path == "/center.html":
    #    result = center()
    #    return result

    #else:
    #    result = not_found()
    #    return result


