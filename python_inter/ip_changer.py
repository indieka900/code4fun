import requests
import os
from time import sleep

def Main(): 
    change = int(input("After hoe much seconds do you want to change your IP: "))
    os.system("service tor start")
    url = "https://httpbin.org/ip"
    proxy = {
        "http" : "socks5://127.0.0.1:9050",
        "https" : "socks5://127.0.0.1:9050"
    }
    
    while True:
        req = requests.get(url, proxies=proxy)
        if req.status_code == 200:
            print(req.json())
        else:
            print("Failed to get current ip")
            print(f"\n {req.json()}")
        sleep(change)
        os.system("service tor reload")
        
if __name__ == "__main__":
    Main()