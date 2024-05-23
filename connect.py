import urllib.request

url = "https://135.181.96.160:44445"
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(url, context=context) as response:
    print("Connection successful!")