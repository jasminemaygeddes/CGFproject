import requests 
import random

# get pockemon data dictionary
def getPockemon(id):

    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    responce = requests.get(url)
    pockemon = responce.json()

    return {
        'name': pockemon['name'],
        'id': pockemon['id'],
        'height': pockemon['height'],
        'weight': pockemon['weight']
    }

# get random ID number
def chosePockemon():
    return random.randint(1, 151)

def showResults(list, param, res1, res2):
    print('Your opponent pockemon:')
    showPockemon(list)
    print()
    print(f'Your {param} is: {res1}')
    print(f'Your opponent {param} is: {res2}')

def showPockemon(dict):
    print(f"Name: {dict['name']}")
    print(f"Id: {dict['id']}")
    print(f"Weight: {dict['weight']}")
    print(f"Height: {dict['height']}")

# getting pockemon from the computer list with max param value
def computerPockemon(list, param):
    paramValueList = []
    for i in range(len(list)):
        paramValueList.append(list[i][param])
    maxValue = max(paramValueList)

    for i in range(len(list)):
        if list[i][param] == maxValue:
            return list[i]

# getting chosen pockemon from the user's pockemon list
def findUserPockemon(list, number):
    return list[number]

# getting full key name for pockemon's dictionary
def defineParameter(data):
    if data == 'h':
        return 'height'
    elif data == 'w':
        return 'weight'
    else:
        return data
    
# check chosen pockemon card if it's in playing cards range
def checkPockemonNumber(num, totalNum):
    if num > totalNum or num < 1:
        print(f'Wrong number! You have only {totalNum} pockemons')
        return False
    else:
        return True

#check the input of chosen parameter
def checkParameter(input):
    if input == 'id' or input == 'w' or input == 'h':
        return True
    else: 
        print('Wrong parameter!')
        return False 
