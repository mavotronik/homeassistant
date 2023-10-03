import requests

token = data.get("token")
temperature = data.get("temperature")
humidity = data.get("humidity")
pressure = data.get("pressure")

resp = requests.get(f"https://stations.windy.com/pws/update/{token}?si=0&temp={temperature}&humidity={humidity}&mbar={pressure}")
# logger.warning(resp.text)