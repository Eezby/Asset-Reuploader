import subprocess, os
from datetime import datetime

# Output colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# File types
FILE_TYPE_MAPPING = {
    "audio": ".mp3",
    "3": ".mp3"
}

# Required files
assetFile = None
cookiesFile = None
for file in os.listdir("./"):
    if file.endswith(".txt"):
        if file.startswith("cookies"):
            cookiesFile = open(file, "r")
        else:
            assetFile = open(file, "r")

if assetFile is None:
    print(bcolors.FAIL + "Could not find .txt file with list of asset IDs and names" + bcolors.ENDC)
    quit()

if cookiesFile is None:
    print(bcolors.FAIL + "No cookies.txt file was found, one must exist to run this process" + bcolors.ENDC)
    quit()

# Create a new folder named after the current timestamp
currentTime = datetime.now()
directory = "Assets/" + str(currentTime.year) + "-" + str(currentTime.month) + "-" + str(currentTime.day) + "-" + str(currentTime.hour) + "-" + str(round(currentTime.second))
if not os.path.exists(directory):
    os.makedirs(directory)

    totalAssetCount = len(assetFile.readlines())
    processedAssetCount = 0

    # Reset pointer back to start of file
    assetFile.seek(0)

    # Read through asset list text file line by line
    for asset in assetFile.readlines():
        asset = asset.strip()           # Gets rid of new line
        components = asset.split(" ")   # Separate string into array
        id = components[0]
        name = components[1]
        assetType = str(components[2]).lower()

        processedAssetCount += 1
        counterText = "(" + str(processedAssetCount) + "/" + str(totalAssetCount) + ") "

        # If the file type doesn't exist in the mapping throw a warning and skip
        if not assetType in FILE_TYPE_MAPPING.keys():
            print(bcolors.WARNING + counterText + assetType + " (" + id + "/" + name + ") is not yet supported" + bcolors.ENDC)
            continue

        fileType = FILE_TYPE_MAPPING[assetType]
        fileTypeDirectory = directory + "/" + assetType

        # Make a new folder named after the asset type
        if not os.path.exists(fileTypeDirectory):
            os.makedirs(fileTypeDirectory)
        try:
            subprocess.run("rbxmk download-asset --id " + id + " " + fileTypeDirectory + "/" + name + fileType + " " + "--cookies-file " + cookiesFile.name)
        except:
            print(bcolors.FAIL + counterText + "An error occured when trying to download asset " + "(" + id + "/" + name + ")" + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + counterText + "Downloaded " + id + "/" + name + bcolors.ENDC)
        
else:
    print(bcolors.FAIL + "Folder already exists, delete or re-name it before trying again" + bcolors.ENDC)
    quit()

input("Press 'Enter' to exit")
