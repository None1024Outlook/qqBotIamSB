import requests

def get_status(url):
    return requests.get(url=f"{url}/get_status").json()["data"]
