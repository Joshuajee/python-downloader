import downloader
import storage

url = input("Please Enter Url to file: ")
ext = input("Please Enter File extension: ")

try:
    download = downloader.downloader(url, ext)
    storage  = storage.storage(download[0], download[1])
except:
    print("An error occurred")