import requests as http
import json, time

securityKey = input("ROBLOSECURITY (only include number and letter characters): ")
# assetIds = input("List of asset IDs (use ',' as delimiter): ")

def reuploadAsset(id, requestData, sleepTime):
    print('test')


# Attempt to log out the user from Roblox, this will fail, but give a valid x-csrf-token
httpSession = http.Session()
httpSession.cookies[".ROBLOSECURITY"] = securityKey
response = httpSession.post("https://auth.roblox.com/v2/logout")
token = response.headers["x-csrf-token"]
httpSession.close()

# Iterate through sound IDs and put universe ID in permissions
httpSession = http.Session()
httpSession.cookies[".ROBLOSECURITY"] = securityKey
httpSession.headers["x-csrf-token"] = token
httpSession.headers["Content-Type"] = "application/json"

file = open("Assets/test.mp3", "rb")

requestData = {
    "requests": [
        {
        "name": "TEST",
        "file": file,
        "groupId": 6620912,
        "assetPrivacy": "Private"
        }
    ]
}

response = httpSession.post("https://publish.roblox.com/v1/audio", data = json.dumps(requestData))
print(response)
print(response.content)
print(response.text)

# assetIds.replace(" ", "")
# assetIdList = assetIds.split(",")


# for id in assetIdList:
#     reuploadAsset(id, requestData, 0)


# input("Press 'Enter' to exit")