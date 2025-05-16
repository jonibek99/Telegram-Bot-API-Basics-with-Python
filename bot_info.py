import requests
from config import TOKEN, BASE_URL


def get_bot_info():
    """
    Task 1: Get Bot Information
    - Use getMe method
    - Return bot's name and username
    - Show verification status
    """
    response = requests.get(f"{BASE_URL}/getMe")
    data=response.json()
    use=data['result']
    h = use["first_name"]
    usern = use["username"]
    #massege=updates["username"]
  #  last=massege[ "username"]
    print(h,usern)
get_bot_info()
