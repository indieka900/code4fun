import requests

def send_req(username, displayName):
    url = 'http://localhost:3000/api/adduser'
    payload = {
        "username": username,
        "displayName": displayName
    }
    response = requests.post(url,data=payload)
    if response.status_code == 201:
        print(f"The message was send")
    else:
        print(f"The request was not sent")
        
send_req("Joseph In","JJ123")
send_req("Joseph Ali","J254")
send_req("Joseph Amos","Amo_J")