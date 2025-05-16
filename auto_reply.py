# import requests
from config import TOKEN, BASE_URL

# reply_to_last_user()
import requests

def reply_to_last_user():
    response = requests.get(f"{BASE_URL}/getUpdates")
    data=response.json()
    updates=data['result'][-1]
    chat_id = updates['message']['chat']['id']
    massege = updates['message']['text'].lower()

    if 'hi' in massege:
        reply_text = 'Hello!'
    elif 'by' in massege:
        reply_text = 'Goodbye!'
    else:
        reply_text ='xato'
    send_url = BASE_URL + "/sendMessage"
    requests.post(send_url, params={'chat_id': chat_id,'text':reply_text })
    print(send_url)
reply_to_last_user()

