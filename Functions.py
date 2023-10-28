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
        'id': starwars['id'],
        'height': starwars['height'],
        'weight': starwars['mass']
    }

# draw a random number(s) between 1 and 83
def Choose_Card():
  return random.randint(1, 83)

  
def showCards(dict):
    print(f"Name: {dict['name']}")
    print(f"Id: {dict['id']}")
    print(f"Weight: {dict['weight']}")
    print(f"Height: {dict['height']}")