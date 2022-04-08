#from email.mime import message
import os, json, requests, time, sqlite3
from urllib import response
import re

from flask import Flask, request, abort
from config import *
#from pyngrok import conf, ngrok

app = Flask(__name__)
app.config['DEBUG'] = True

def ReplyMessage(Reply_token, TextMessage, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Access_Token) # Channel Access Token
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }
    data = json.dumps(data)
    requests.post(LINE_API, headers=headers, data=data)
    return 200


def get_telephone_data(name):
    conn = sqlite3.connect('02_telephone.db')
    c = conn.cursor()

    # sql = "SELECT * FROM telephone WHERE name like '%{}%'".format(name)
    
    try:
        sql = "SELECT * FROM telephone WHERE name like '%{}%'".format(name)
        c.execute(sql)
        data = c.fetchall()
        if not data:
            sql = "SELECT * FROM telephone WHERE place like '%{}%'".format(name)
            c.execute(sql)
            data = c.fetchall()
        return data
        c.close()
    except:
        data = []
    return data
    # conn.close()
    
@app.route('/get_phone', methods=['GET', 'POST'])
def telephone_data():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        name = data['events'][0]['message']['text']
        Reply_token = data['events'][0]['replyToken']
        print(name)
        phone = get_telephone_data(name)
        print(phone)
        
        reply_message = ''
        if phone:
            for i in phone:
                reply_message += 'หน่วย : {}\n'.format(i[1]) + 'สถานที่ : {}\n'.format(i[2]) + ('สส.ทหาร: {}\n'.format(i[3]) if i[3] else 'สส.ทหาร: ไม่มีข้อมูล\n') + ('ภายใน ทบ.: {}\n'.format(i[4]) if i[4] else 'ภายใน ทบ.: ไม่มีข้อมูล\n') + ('จนท.ประจำหน่วย : {}\n'.format(i[5]) if i[5] else 'จนท.ประจำหน่วย : ไม่มีข้อมูล\n') + ('-'*23) + ('\n')
            ReplyMessage(Reply_token, reply_message, channel_access_token)
        else:
            reply_message = 'ไม่พบข้อมูล : {}'.format(name)
            ReplyMessage(Reply_token, reply_message, channel_access_token)
        return request.json, 200
    elif request.method == 'GET':
        return 'Ok', 200
    else:
        abort(400)

@app.route('/')
def hello():
    return "Hello"
    
if (__name__ == '__main__'):
    app.run(host='127.0.0.1', port=5000)
