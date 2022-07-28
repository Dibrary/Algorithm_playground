
import requests
# response = requests.get("http://localhost:3000/memo")
# print(response)
# print(response.json())


response = requests.post("http://localhost:3000/memo", data={'name': 'Test User', "body":"Chicken"})
print(response)
print(response.json())

'''
처음에 만들어 놓은 json-server의 기반 json파일 내용이
{
  "memo": [
    {
      "id": 1,
      "title": "Pizza",
      "body": "Cheese"
    }
  ]
}
이렇게 되어 있어서 memo로 데이터를 넣을 수 있다. 데이터 넣고 나면
{
  "memo": [
    {
      "id": 1,
      "title": "Pizza",
      "body": "Cheese"
    },
    {
      "name": "Test User",
      "body": "Chicken",
      "id": 2 # 이렇게 id가 자동으로 할당된다.
    }
  ]
}
'''
