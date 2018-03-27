import requests

# put your keys in the header
headers = {
    "app_id": "268b55b2",
    "app_key": "7cf6f27d241f5fb1b1ba1e3f98af0f77"
}

# payload = '{"image":"https://media.kairos.com/liz.jpg"}'
payload = '{"image":"camera.png"}'
url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print(r.content)