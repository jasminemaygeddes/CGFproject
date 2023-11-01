import requests
import random

def getCharacter():
    """
    Function to get a random character details from the Harry Potter API
    """
    url = 'https://hp-api.onrender.com/api/characters/students'  # Updated URL
    response = requests.get(url)
    character = random.choice(response.json())
    return {
        'name': character.get('name', 'Unknown'),
        'house': character.get('house', 'Unknown'),
        'patronus': character.get('patronus', 'Unknown'),
        'eyeColour': character.get('eyeColour', 'Unknown'),
    }
def showCharacter(character):
    """
    Function to show the details of a character
    """
    print(f"Name: {character['name']}")
    print(f"House: {character['house']}")
    print(f"Patronus: {character['patronus']}")
    print(f"eyeColour: {character['eyeColour']}")

def showResults(opponent_character, param, user_result, opponent_result):
    """
    Function to show the results of the game
    """
    print(f'Your opponent character:')
    showCharacter(opponent_character)
    print()
    print(f'Your {param} is: {user_result}')
    print(f'Your opponent {param} is: {opponent_result}')

def computerCharacter(characters_list, param):
    """
    Function to choose the computer's character
    """
    param_value_list = []
    for character in characters_list:
        param_value_list.append(character[param])
    max_value = max(param_value_list)

    for character in characters_list:
        if character[param] == max_value:
            return character

def findUserCharacter(characters_list, number):
    """
    Function to find the user's character
    """
    return characters_list[number]

computerScore = 0
userScore = 0
answer = 'y'
greetingMsg = "Welcome to the Harry Potter game! Let's play?(y/n): "

while answer == 'y':
    userAnswer = input(greetingMsg)
    answer = userAnswer
    greetingMsg = 'Do you want to play again?(y/n): '

    if userAnswer == 'y':

        userCharacterList = []
        computerCharacterList = []

        cardsNumber = int(input('How many cards do you want to play with?: '))

        if cardsNumber > 1:
            userCharacterList = []
            computerCharacterList = []

            print('\nYour characters:')

            for i in range(cardsNumber):
                userCharacterList.append(getCharacter())

                print(f'\nCharacter number {i + 1}:\n')
                showCharacter(userCharacterList[i])
                computerCharacterList.append(getCharacter())
                computerCharacterList.append(getCharacter())

            print('\n')
            userCardChoice = int(input('Choose the character number: '))
            userParamChoice = input('Choose parameter:(name, house, patronus) ')

            computerCard = computerCharacter(computerCharacterList, userParamChoice)
            userCard = findUserCharacter(userCharacterList, userCardChoice - 1)
            print()

            print(f'You choose: {userCard["name"].upper()}!')
            showCharacter(userCard)
            print()

            print('Your opponent character cards:')
            for character in computerCharacterList:
                showCharacter(character)
                print()

            userResult = userCard[userParamChoice]
            compResult = computerCard[userParamChoice]

            if userResult > compResult:
                userScore += 1
                showResults(computerCard, userParamChoice, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                showResults(computerCard, userParamChoice, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                showResults(computerCard, userParamChoice, userResult, compResult)
                print(f'Equal! The score is: {userScore}/{computerScore}')

        else:
            print(f'Your character: ')
            userCharacter = getCharacter()
            showCharacter(userCharacter)
            userParamChoice = input('Choose parameter:(name, house, patronus) ')
            print()

            userResult = userCharacter[userParamChoice]
            compCharacter = getCharacter()
            compResult = compCharacter[userParamChoice]

            if userResult > compResult:
                userScore += 1
                showResults(compCharacter, userParamChoice, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                showResults(compCharacter, userParamChoice, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                print(f'Equal! The score is: {userScore}/{computerScore}')

    else:

        print(f'The final score is: {userScore}/{computerScore}\nGoodbye!')