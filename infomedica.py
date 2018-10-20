import infermedica_api

api = infermedica_api.API(app_id = '059ee519', app_key = '82d0384c0192bf00021a4eda9846503b')

import requests
sex = input("What is your sex? ")
age = input("What is your age? ")
symptoms = input("What symptoms are you feeling? ")
headers = {
    'App-Id': '059ee519',
    'App-Key': '82d0384c0192bf00021a4eda9846503b',
    'Content-Type': 'application/json',
}

data = '{"text": \"' +symptoms +'\"}'

response = requests.post('https://api.infermedica.com/v2/parse', headers=headers, data=data)

response = response.json()
print(response)
#print(response['mentions'][0]['id'])

id = response['mentions'][0]['id']
choiceid = response['mentions'][0]['choice_id']
headers = {
    'App-Id': '059ee519',
    'App-Key': '82d0384c0192bf00021a4eda9846503b',
    'Content-Type': 'application/json',
}

data = '{\n    "sex": \"'+sex+'\",\n    "age":'+age+',\n    "evidence": [\n      {"id": \"' +id + '\", "choice_id": \"'+choiceid + '\"}\n  ]\n  }'

response = requests.post('https://api.infermedica.com/v2/diagnosis', headers=headers, data=data)

response = response.json()
print(response)
