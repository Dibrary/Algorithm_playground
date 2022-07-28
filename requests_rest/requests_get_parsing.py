
import requests
# json으로 가져와서 파싱 해 보자.

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.json())

json_value = response.json()
print(json_value.keys()) # 전체 key가 뭐뭐 있는지 확인
length = len(json_value.keys())

for idx, i in zip(range(length), json_value.keys()): # 인덱스도 같이 뽑아서 확인
    print(f"{list(json_value.keys())[idx]},    {json_value.get(i)},    {type(json_value.get(i))}")
    # 중간에 여러 값을 가진 key의 경우는 해당 값이 또 dict 형으로 이뤄진 것을 볼 수 있다.

'''
{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}
dict_keys(['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company'])
id,    1,    <class 'int'>
name,    Leanne Graham,    <class 'str'>
username,    Bret,    <class 'str'>
email,    Sincere@april.biz,    <class 'str'>
address,    {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}},    <class 'dict'>
phone,    1-770-736-8031 x56442,    <class 'str'>
website,    hildegard.org,    <class 'str'>
company,    {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'},    <class 'dict'>

이렇게 출력됨.
'''

import requests
# json으로 가져와서 파싱 해 보자.

with open("JSONdata.json", "w", encoding='utf-8') as f:
    for m in range(1, 10): # users는 10개가 있다고 함.
        response = requests.get("https://jsonplaceholder.typicode.com/users/"+str(m))

        # json_value = response.json() # 이런 꼴로는 파일에 쓸 수 없음.
        # print(json_value.keys()) # 전체 key가 뭐뭐 있는지 확인
        # length = len(json_value.keys())
        f.write(response.text + ",\n") # 그냥 이렇게만 하면 [ ] 는 없어서 json파일을 다시 read하는게 안 된다. (수작업으로 수정을 해줘야 함)

        # for idx, i in zip(range(length), json_value.keys()): # 인덱스도 같이 뽑아서 확인
        #     print(f"{list(json_value.keys())[idx]},    {json_value.get(i)},    {type(json_value.get(i))}")
