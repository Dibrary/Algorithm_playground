import requests

# 사용한 대응 사이트는 https://jsonplaceholder.typicode.com/

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print("=====")
print(response.content) # 바이너리 원문을 얻을 수 있다.
print("=====")
print(response.text) # UTF-8 원문을 얻을 수 있다.
print("=====")
print(response.json())



