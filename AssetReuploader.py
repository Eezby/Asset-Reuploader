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

response = httpSession.get("https://assetdelivery.roblox.com/v1/asset/?id=11558867190")
print(response.status_code)
print(response.content)

# assetIds.replace(" ", "")
# assetIdList = assetIds.split(",")


# for id in assetIdList:
#     reuploadAsset(id, requestData, 0)


# input("Press 'Enter' to exit")