from game_functions import getCharacter, showCharacter, show_Results, computerPockemon
from game_functions import findUserPockemon, compareEyes

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

            print('\n')
            userCardChoice = int(input('Choose the character number: '))
            userParamChoice = input('Choose parameter:(name, house, patronus, eye color) ')
            if userParamChoice == 'eye color':
                userParamChoice = 'eyeColour'

            computerCard = computerPockemon(computerCharacterList, userParamChoice)
            userCard = findUserPockemon(userCharacterList, userCardChoice - 1)
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
            
            if userParamChoice == 'eye color':
                result = compareEyes(userCard['eyeColor'], computerCard['eyeColor'])
                if result == 1:
                    userScore += 1
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'You won! The score is: {userScore}/{computerScore}')
                elif result == 0:
                    computerScore += 1
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'You lose. The score is: {userScore}/{computerScore}')
                else:
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'Equal! The score is: {userScore}/{computerScore}')
            else:
                if userResult > compResult:
                    computerScore += 1
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'You lose. The score is: {userScore}/{computerScore}')
                elif userResult < compResult:
                    userScore += 1
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'You won! The score is: {userScore}/{computerScore}')
                else:
                    show_Results(computerCard, userParamChoice, userResult, compResult)
                    print(f'Equal! The score is: {userScore}/{computerScore}')

        else:
            print(f'Your character: ')
            userCharacter = getCharacter()
            showCharacter(userCharacter)
            userParamChoice = input('Choose parameter:(name, house, patronus, eye color) ')
            print()
            if userParamChoice == 'eye color':
                userParamChoice = 'eyeColour'

            userResult = userCharacter[userParamChoice]
            compCharacter = getCharacter()
            compResult = compCharacter[userParamChoice]
            
            # if user's chosen parameter is an eye color
            if userParamChoice == 'eye color':
                result = compareEyes(userCard['eyeColor'], computerCard['eyeColor'])
                if result == 1:
                    userScore += 1
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'You won! The score is: {userScore}/{computerScore}')
                elif result == 0:
                    computerScore += 1
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'You lose. The score is: {userScore}/{computerScore}')
                else:
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'Equal! The score is: {userScore}/{computerScore}')
            else:

                # if chosen other parameters
                if userResult > compResult:
                    computerScore += 1
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'You lose. The score is: {userScore}/{computerScore}')
                elif userResult < compResult:
                    userScore += 1
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'You won! The score is: {userScore}/{computerScore}')
                else:
                    show_Results(compCharacter, userParamChoice, userResult, compResult)
                    print(f'Equal! The score is: {userScore}/{computerScore}')

    else:

        print(f'The final score is: {userScore}/{computerScore}\nGoodbye!')
