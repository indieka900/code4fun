import requests

# https://realpython.com/python-requests/

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
        
# res = requests.get("https://api.github.com")
res = requests.get("http://localhost:3000/api/users")
res1 = requests.get("http://localhost:3000/api/user",params={"id":2})
# print(res)
# print(res.text)
# print(res.content)

data = res.json()
# print(data[1]["username"])

data1 = res1.json()
# print(f'{res1.status_code} -- {data1['username']}')

# Search GitHub's repositories for popular Python projects
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)

# Inspect some attributes of the first three repositories
json_response = response.json()
popular_repositories = json_response["items"]
for repo in popular_repositories[:5]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print()