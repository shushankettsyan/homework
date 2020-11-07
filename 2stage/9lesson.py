import requests
import json

# response = requests.get("https://xkcd.com/353/")
# response_2 = requests.get("https://xkcd.com/353sdfsdjfsjdfskfdhjdfahjdhhjdf/")
# print(dir(response))

# print(help(response))

# print(F"the status code of request is {response.status_code}")

# print(F"thr URL of the request is {response.url}")

# print(F"the text of the request is:\n\n{response.text}")
#
# print(F"the text of the request is:\n\n{response.content}")

# response = requests.get("http://www.httpbin.org/image/jpeg")
# response_2 = requests.get("http://www.httpbin.org/image/png")
#
#
# with open("new1_photo.jpeg", "wb") as file:
#     file.write(response.content)
#
# with open("new2_photo.png", "wb") as file:
#     file.write(response_2.content)

# print(response.content)
# print(response_2.content)


# parameters = {"name":"python","school":"basic IT"}
#
# response = requests.get("https://httpbin.org/get", params = parameters)
# print(response.url)
# print(response.text)
#
# r = response.json()
# print(type(r))
# print(r["args"]["name"])
##-------------------------------------------------------------------------------
dict_ = {
    "name":"Scarlett",
    "surname":"Johansson",
    "age":35,
    "height": 1.6,
    "married": False,
    "movies": ["Black Widow","Lucy","The Avengers","The Other Boleyn Girl"]
    }

response =  requests.post("https://httpbin.org/post", json = dict_)
data = json.dumps(dict_)
print(response)
print(response.text)
