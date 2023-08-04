import requests

resp = requests.post("http://localhost:5000/predict", files={'file': open('test_images/N.jpg', 'rb')})

print(resp.text)
