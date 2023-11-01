import requests 
import random

# POCKEMON GAME
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
    
#HARRY POTTER GAME
# function to get a random character details from the Harry Potter API
def getCharacter():

    url = 'https://hp-api.onrender.com/api/characters/students'  # Updated URL
    response = requests.get(url)
    character = random.choice(response.json())
    return {
        'name': character.get('name', 'Unknown'),
        'house': character.get('house', 'Unknown'),
        'patronus': character.get('patronus', 'Unknown'),
        'eyeColour': character.get('eyeColour', 'Unknown'),
    }

# function to show the details of a character
def showCharacter(character):

    print(f"Name: {character['name']}")
    print(f"House: {character['house']}")
    print(f"Patronus: {character['patronus']}")
    print(f"eyeColour: {character['eyeColour']}")

# function to show the results of the game
def show_Results(opponent_character, param, user_result, opponent_result):

    print(f'Your opponent character:')
    showCharacter(opponent_character)
    print()
    print(f'Your {param} is: {user_result}')
    print(f'Your opponent {param} is: {opponent_result}')

def compareEyes(col1='blue', col2='blue'):
    if col1 == '':
        col1 = 'blue'
    elif col2 == '':
        col2 = 'blue'

    if col1 == 'blue' and (col2 == 'brown' or col2 == 'black'):
        return 1
    elif col1 == 'black' and (col2 == 'brown' or col2 == 'green' or col2 == 'grey'):
        return 1
    elif col1 == 'brown' and (col2 == 'green' or col2 == 'grey'):
        return 1
    elif col1 == 'green' and (col2 == 'grey' or col2 == 'blue'):
        return 1
    elif col1 == 'grey' and col2 == 'blue':
        return 1
    elif col1 == col2:
        return 2
    else:
        return 0
    
# STAR WARS GAME

# get StarWars data dictionary - this just pulls the data for the human and human-like characters
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

def show_results(list, param, res1, res2):
    print("Your opponent's characters")
    showCards(list)
    print()
    print(f'Your {param} is: {res1}')
    print(f"Your opponent's {param} is: {res2}")