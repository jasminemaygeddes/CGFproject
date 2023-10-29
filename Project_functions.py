#define necessary functions here for the Top Trumps game.
import requests
import random
#get StarWars data dictionary - this just pulls the data for the human and human-like characters

def getStarwars(id):

    url = f'https://swapi.dev/api/people/{id}/'
    response = requests.get(url)
    starwars = response.json()

    return {
        'name': starwars['name'],
        'height': starwars['height'],
        'weight': starwars['mass']
    }

# draw a random number(s) between 1 and 83
def Choose_Card():
  return random.randint(1, 83)

# print the info for each card drawn  
def showCards(dict):
    print(f"Name: {dict['name']}")
    print(f"Weight: {dict['weight']}")
    print(f"Height: {dict['height']}")

def showResults2(list, param, res1, res2):
    print('Your opponent pockemon:')
    showCards(list)
    print()
    print(f'Your {param} is: {res1}')
    print(f'Your opponent {param} is: {res2}')

# getting pockemon from the computer list with max param value
def computerCards(list, param):
    paramValueList = []
    for i in range(len(list)):
        paramValueList.append(list[i][param])
    maxValue = max(paramValueList)

    for i in range(len(list)):
        if list[i][param] == maxValue:
            return list[i]

# getting chosen card from the user's character list
def findUserCharacter(list, number):
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
def checkCardNumber(num, totalNum):
    if num > totalNum or num < 1:
        print(f'Wrong number! You have only {totalNum} cards')
        return False
    else:
        return True

#check the input of chosen parameter
def checkParameter(input):
    if input == 'id' or input == 'w' or input == 'h':
        return True
    else: 
        print('Incorrect parameter. Try again.')
        return False 
