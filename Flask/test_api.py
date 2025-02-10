import requests
url = "http://127.0.0.1:8000/user/3"
data = {"name"  :"Sounak" , "age"  :22}

response  =requests.get(url, json=data)
print(response.json())
