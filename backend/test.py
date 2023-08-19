import requests

thumb = f'https://i.ytimg.com/vi/{requests.get("https://youtu.be/fjdrbqN5e-0").url.split("v=")[1]}/hqdefault.jpg'

print(requests.get("https://youtu.be/fjdrbqN5e-0").url)

print(thumb)