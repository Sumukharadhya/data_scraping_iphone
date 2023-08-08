import requests


def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w")as f:
        f.write(r.text)


url = "https://timesofindia.indiatimes.com/?from=mdr"

fetchAndSaveToFile(url, "data/times.html")
