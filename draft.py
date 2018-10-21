import infermedica_api
import requests
import json

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


sex = input("What is your sex? (male, female, rather not say) \n")
sex = sex.lower()
while sex != 'male' and sex!='female' and sex!='rather not say':
    print("That was not one of the three options \n")
    sex = input("What is your sex? (male, female, rather not say) \n")
    sex = sex.lower()

age = input("What is your age? (number or rather not say) \n")
properAge = False
while properAge == False:
    if RepresentsInt(age) == True:
        if int(age) < 1:
            print("Your response was not one of the accepted options")
            age = input("What is your age? (number or rather not say) \n")
        elif int(age)>122:
            print("Your response was not one of the accepted options")
            age = input("What is your age? (number or rather not say) \n")
        else:
            properAge = True
    else:
        if age != "rather not say":
            print("Your response was not one of the accepted options")
            age = input("What is your age? (number or rather not say) \n")
        else:
            properAge = True


if sex == "rather not say":
    sex = "male"
if age == "rather not say":
    age = 30

symptoms = input("What symptoms are you feeling? \n")
headers = {
    'App-Id': '059ee519',
    'App-Key': '82d0384c0192bf00021a4eda9846503b',
    'Content-Type': 'application/json',
}

data = '{"text": \"' +symptoms +'\"}'

response = requests.post('https://api.infermedica.com/v2/parse', headers=headers, data=data)


response = response.json()

while len(response['mentions'])==0:
    print("That symptom was invalid\n")
    symptoms = input("What symptoms are you feeling? \n")
    data = '{"text": \"' +symptoms +'\"}'
    response = requests.post('https://api.infermedica.com/v2/parse', headers=headers, data=data)
    response = response.json()

numOfIntialSymptoms = len(response['mentions'])
data = '{\n    "sex": \"'+sex+'\",\n    "age":'+age+',\n    "evidence": [\n'
initialSymptoms = []
for value in range(0,numOfIntialSymptoms):
    id = response['mentions'][value]['id']
    choiceid = response['mentions'][value]['choice_id']
    idPair = [id, choiceid]
    initialSymptoms.append(idPair)


data = '{\n    "sex": \"'+sex+'\",\n    "age":'+age+',\n    "evidence": [\n      '
for value in range(0, numOfIntialSymptoms):
    data = data + '{"id": \"' +initialSymptoms[value][0] + '\", "choice_id": \"'+initialSymptoms[value][1] + '\"}\n  ]\n  }'
    response = requests.post('https://api.infermedica.com/v2/diagnosis', headers=headers, data=data)
    data = data[:-8]
    data = data + ","

data = data[:-1]
data = data + '  ]\n  }'
responsej = response.json()
probability = responsej['conditions'][0]['probability']

while(probability < 0.75):
    numOfQuestions = len(responsej['question']['items'])    ,
    print(responsej['question']['text'] + "\n")
    for value in range(0,numOfQuestions):
        if(numOfQuestions>1):
            print(str(value+1))
        print(responsej['question']['items'][value]['name'])
    print("\n")

    if numOfQuestions == 1:
        questionResponse = input("Answer with Yes, No, or I don\'t know \n")
        questionResponse = questionResponse.lower()
        if questionResponse == "idk" or questionResponse == "i dont know":
            questionResponse = "i don\'t know"
        while questionResponse != "yes" and questionResponse != "no" and questionResponse != "i don\'t know":
            print("Your answer is invalid \n")
            questionResponse = input("Answer with Yes, No, or I don\'t know \n")
            questionResponse = questionResponse.lower()
            if questionResponse == "idk" or questionResponse == "i dont know":
                questionResponse = "i don\'t know"
    else:
        questionResponse = input("Answer with the number of the correct answer \n")
        properIntAnswer = False
        while properIntAnswer == False:
            if RepresentsInt(questionResponse) == True:
                questionResponse = int(questionResponse)
                if questionResponse < 1:
                    print("Your answer is not a valid option")
                    questionResponse = input("Answer with the number of the correct answer \n")
                elif questionResponse > numOfQuestions:
                    print("Your answer is not a valid option")
                    questionResponse = input("Answer with the number of the correct answer \n")
                else:
                    properIntAnswer = True;
            else:
                print("Your answer must be a number")
                questionResponse = input("Answer with the number of the correct answer \n")


    if questionResponse == "yes":
        questionIndex = 0
    elif questionResponse == "no":
        questionIndex = 0
    elif questionResponse == "i don\'t know":
        questionIndex = 0
    else:
        questionIndex = questionResponse-1

    for value in responsej['question']['items']:
        if questionResponse=="yes" or value==responsej['question']['items'][questionIndex]:
            choiceid = value['choices'][0]['id']
        if questionResponse=="no" or value!=responsej['question']['items'][questionIndex] :
            choiceid = value['choices'][1]['id']
        elif questionResponse == "i don\'t know":

            choiceid = value['choices'][2]['id']

        id = value['id']
        data = data[:-7]
        data = data + ',\n'
        data = data + '{"id": \"' +id + '\", "choice_id": \"'+choiceid + '\"}'
        data = data + '\n  ]\n  }'
        response = requests.post('https://api.infermedica.com/v2/diagnosis', headers=headers, data=data)

    responsej = response.json()
    probability = responsej['conditions'][0]['probability']

print("\n" + responsej['conditions'][0]['name'] + " with a " + str(responsej['conditions'][0]['probability']*100) + "% chance")
