import requests


def fox():
    url = "https://randomfox.ca/floof"

    respons = requests.get(url)

    if respons.status_code == 200:
        return respons.json().get("image")
    else:
        return None

if __name__ == "__main__":
    print(fox())
