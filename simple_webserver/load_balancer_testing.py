import requests

while True:
    res = requests.get('PUT YOUR OWN ELB DNS')
    print(res.text)
