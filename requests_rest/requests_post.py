

import requests

result = requests.post("https://jsonplaceholder.typicode.com/posts", data={'name': 'Test User', "body":"Chicken"})
print(result)
print(result.json())

# 넣은 것을 다시 가져올 수는 없다. 
# 넣는게 되는지만 확인 가능.

value = requests.get("https://jsonplaceholder.typicode.com/posts/100")
print(value.json())



