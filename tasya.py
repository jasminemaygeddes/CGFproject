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
    print(f'Your opponent pockemons:{list}')
    print(f'Your {param} is: {res1}')
    print(f'Your opponent {param} is: {res2}')
