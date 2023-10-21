# import functions
from tasya import getPockemon, chosePockemon, showResults, showPockemon

# start the game
# ask user to play
answer = 'y'
userScore = 0
computerScore = 0
greetingMsg = "Welcome to the Pockemon game! Let's play?(y/n): "

while answer == 'y':
    userAnswer = input(greetingMsg)
    answer = userAnswer
    greetingMsg = 'Do you want to play again?(y/n): '

    if userAnswer == 'y':
        
        userPockemonList = []
        computerPockemonList = []

        cardsNumber = int(input('How many cards do you want?: '))

        if cardsNumber > 1:
            # show user's pockemons
            print('\nYour pockemons:')
            
            for i in range(cardsNumber):
                userPockemonList.append(getPockemon(chosePockemon()))

                print(f'\nPockemon number {i + 1}:\n')
                showPockemon(userPockemonList[i])

                computerPockemonList.append(getPockemon(chosePockemon()))

            print('\n')
            userCardChoise = input('Chose the pockemon number: ')    
            userParamChoise = input('Choose parameter:(id, height, weight) ')

        else:
            print(f'Your pockemon: {showPockemon(userPockemonList[0])}')
            userParamChoise = input('Choose parameter:(id, height, weight) ')

            # compare parameters
            userResult = userPockemonList[0][userParamChoise]
            compResult = computerPockemonList[0][userParamChoise]

            if userResult > compResult:
                userScore += 1
                showResults(computerPockemonList, userParamChoise, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                showResults(computerPockemonList, userParamChoise, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                print(f'Equal! The score is: {userScore}/{computerScore}')

    else:
        print(f'The final score is: {userScore}/{computerScore}\nGoodbye!')

