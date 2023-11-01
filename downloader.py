import requests


def downloader(url, ext):
    response = requests.get(url)
    if response.status_code == 200:
        return (response.content, ext)
    else: 
        raise("Request Failed")