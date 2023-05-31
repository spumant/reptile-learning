import requests

session = requests.session()

data = {
    "loginName": "18703819187",
    "password": "123456"
}

url = "https://passport.17k.com/ck/user/login"

session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")

print(resp.json())

