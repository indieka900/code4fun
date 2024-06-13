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
        
res = requests.get("https://api.github.com")
#print(res)
print(res.text)