# import requests
from config import TOKEN, BASE_URL


# def reply_to_last_user():
#     """
#     Task 3: Auto-Reply System
#     - Get most recent update
#     - Extract chat_id
#     - Send response message
#     """
#     TOKEN='7908519478:AAGWAJ14YjDrrAu5UeYKUmESP5xTONj5I'
#     BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
#     response=requests.get(f"{BASE_URL}/getUpdates")
#     data=response.json()
#     if not data.get('result'):
#         print('no massage')
#         return 
#     last=data['result'][-1]
#     chat_id=last['massege']['id']
#     requests.post(f"{BASE_URL}/sendMessage",data={'chat_id':data['chat_id'],'text':'bu men egang'})
#     print('javob yuoruldi')
# reply_to_last_user()
import requests

def reply_to_last_user():

    response = requests.get(f"{BASE_URL}/getUpdates")
    data=response.json()
    updates=data['result'][-1]
    massege=updates['message']['chat']['id']
    sender=BASE_URL+"/sendMessage"

    requests.post(sender,params={'chat_id':massege,'text':'ali kut pro max,'})
    return massege

print(reply_to_last_user())
