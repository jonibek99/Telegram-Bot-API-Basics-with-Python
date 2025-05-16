import requests
from config import TOKEN, BASE_URL
def handle_message(message):
    """
    Optional Challenge: Conditional Responses
    - Handle different message inputs
    - Return appropriate responses
    """
    response = requests.get(f"{BASE_URL}/getUpdates")
    data=response.json()
    updates=data['result'][-1]
    massege=updates['message']['text']
    sendler=BASE_URL+"/sendMessage"

    requests.post(sendler,params={'chat_id':massege, 'hello':'by'})
    if 'hi' in sendler:
        return 'hello'
    elif 'by':
     return 'gppdb'
    print(massege)
handle_message('me')
  