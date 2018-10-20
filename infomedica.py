import infermedica_api

api = infermedica_api.API(app_id = '059ee519', app_key = '82d0384c0192bf00021a4eda9846503b')

import requests
sex = input("What is your sex? \n")
age = input("What is your age? \n")
symptoms = input("What symptoms are you feeling? \n")
headers = {
    'App-Id': '059ee519',
    'App-Key': '82d0384c0192bf00021a4eda9846503b',
    'Content-Type': 'application/json',
}

data = '{"text": \"' +symptoms +'\"}'

response = requests.post('https://api.infermedica.com/v2/parse', headers=headers, data=data)

response = response.json()
#print(response)
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

responsej = response.json()
#print(responsej)
probability = responsej['conditions'][0]['probability']
while(probability < 0.5):
    numOfQuestions = len(responsej['question']['items'])
    #print(numOfQuestions)
    print(responsej['question']['text'] + "\n")
    questionList = []
    for value in range(0,numOfQuestions):
        print(responsej['question']['items'][value]['name'])
        questionList.append(responsej['question']['items'][value]['name'])
    print("\n")
    if numOfQuestions == 1:
        questionResponse = input("Answer with Yes, or No \n")
    else:
        questionResponse = input("Answer with the number of the correct answer starting at 1 \n")

    if questionResponse == "Yes":
        questionIndex = 0
        choiceid = responsej['question']['items'][questionIndex]['choices'][0]['id']
    elif questionResponse == "No":
        questionIndex = 0
        choiceid = responsej['question']['items'][questionIndex]['choices'][1]['id']
    else:
        questionIndex = int(questionResponse)-1
        choiceid = responsej['question']['items'][questionIndex]['choices'][0]['id']


    id = responsej['question']['items'][questionIndex]['id']
    data = data[:-8]
    data = data + ',\n'
    data = data + '{"id": \"' +id + '\", "choice_id": \"'+choiceid + '\"}'
    data = data + '\n  ]\n  }'

    response = requests.post('https://api.infermedica.com/v2/diagnosis', headers=headers, data=data)
    responsej = response.json()
    probability = responsej['conditions'][0]['probability']

print("\n" + responsej['conditions'][0]['name'] + " with a " + str(responsej['conditions'][0]['probability']*100) + "% chance")
