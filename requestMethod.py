import requests
IP = 'http://192.168.1.109:8000/'


def get():
    response = requests.get(IP)
    print(response.json())
    return response.json()


def post(body):
    data = {'body': body}
    response = requests.post(IP + 'post', data)
    return response.json()


def put():

    response = requests.put(IP+'/disease/get')
    return response.json()
