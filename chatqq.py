import chat
Chat = chat.Chat()
from nqb import bot
from flask import Flask, request
import threading

Bot = bot.Bot()

a = True
def get(text: str, uid: int):
    global a
    a = False
    out = Chat.chat(text=text)
    print(out)
    file = Chat.to_play(text=out)
    print(file)
    file = file.split("\\")[-1]
    print(file)
    print(f"[CQ:record,file=http://127.0.0.1:8000/{file}]")
    Bot.send_private_msg(user_id=uid, message=f"[CQ:record,file=http://127.0.0.1:8000/{file}]")
    a = True

app = Flask(__name__)
@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == "private":
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        print([uid, message])
        if a:
            threading.Thread(target=get, args=(message, uid)).start()
    return 'OK'

app.run(debug=True, host='127.0.0.1', port=5701)
