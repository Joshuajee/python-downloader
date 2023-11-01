import requests


def downloader(url, ext):
    response = requests.get(url)
    # Check if the request was successful
    print(response.status_code)
    if response.status_code == 200:
        return (response.content, ext)
    else: 
        raise("Request Failed")