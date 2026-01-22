import requests

urr = f"http://localhost:8000/api/v1/advert"

#TODO ----- CREAT AND GET -----

# par = {
#   "title": "hello world",
#   "description": "description hw",
#   "price": 1000,
#   "author": "kama",
#   "release_date": "2026-01-21T12:31:26.615Z"
#     }
# resp = requests.post(url=urr, json=par)

# print(resp.status_code)
# print(resp.text)

# data = requests.get(f"{urr}/3")
# print(data.status_code)
# print(data.json())

# TODO ----- SEARCH -----

# param = {"author": "kama"}

# resp = requests.get(f"{urr}", params=param)

# print(resp.status_code)
# print(resp.json())

#TODO ----- UPDATE -----

# param = {"title": "btc", "description": "A peer-to-peer payment system that uses a unit of the same name to record transactions. Cryptographic methods are used to ensure the system's operation and security, and all transaction information between system addresses is available in cleartext.", "price": 88000, "author": "Satoshi Nakamoto", "release_date": "2009-01-21T12:31:26.615Z"}

# resp = requests.patch(url=f"{urr}/1", json=param)
# print(resp.status_code)
# print(resp.json())

# data = requests.get(f"{urr}/1")
# print(data.status_code)
# print(data.json())

#TODO ----- DELETE -----
# resp = requests.delete(url=f"{urr}/2")

# print(resp.status_code)
# print(resp.json())

# data = requests.get(f"{urr}/2")
# print(data.status_code)
# print(data.json())
