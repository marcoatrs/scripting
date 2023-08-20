import requests


def check_internet():
    try:
        requests.get(url="https://www.google.com/", timeout=5)
        print("Connected")
    except requests.ConnectionError:
        print("No connected")


check_internet()
