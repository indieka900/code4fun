import requests

def tricky_sum(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return tricky_sum(n - 1)
    else:
        return n + tricky_sum(n - 2)
    
# print(tricky_sum(5))

def send_sms(phone_no, msg):
    url = "https://textbelt.com/text"
    payload = {
        "phone": phone_no,
        "message": msg,
        "key": "textbelt" #head over to `https://textbelt.com/` create your own key 
    }
    
    res = requests.post(url,data=payload)
    
    print(res.json())
    
send_sms(254713283900,"Hello there")