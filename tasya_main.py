# import functions from tasya.py file
from tasya import getPockemon, chosePockemon, showResults, showPockemon
from tasya import findUserPockemon, computerPockemon

# start the game
# ask user to play
answer = 'y'
userScore = 0
computerScore = 0
greetingMsg = "Welcome to the Pockemon game! Let's play?(y/n): "

# start game 
while answer == 'y':
    userAnswer = input(greetingMsg)
    answer = userAnswer
    greetingMsg = 'Do you want to play again?(y/n): '

    if userAnswer == 'y':
        # ask user how many cards he/she wants to play with
        cardsNumber = int(input('How many cards do you want to play with?: '))

        if cardsNumber > 1:
            # creating empty lists of pockemons for user and computer
            userPockemonList = []
            computerPockemonList = []

            # show user's pockemons
            print('\nYour pockemons:')
            
            for i in range(cardsNumber):
                # fill the user pockemon list and show it to user
                userPockemonList.append(getPockemon(chosePockemon())) 

                print(f'\nPockemon number {i + 1}:\n')
                showPockemon(userPockemonList[i])

                # fill the computer pockemon list
                computerPockemonList.append(getPockemon(chosePockemon())) 

            print()
            userParamChoise = input('Choose parameter:(id, height, weight) ')
            userCardChoise = int(input('Chose the pockemon number: '))   
            
            # getting 1 chosen card from user and with max value computer card
            computerCard = computerPockemon(computerPockemonList, userParamChoise)
            userCard = findUserPockemon(userPockemonList, userCardChoise - 1)
            print() 

            print(f'You choose: {userCard["name"].upper()}!')
            showPockemon(userCard)
            print()
            
            # show computer pockemon cards
            print('Your opponent pockemon cards:')
            for i in range(len(computerPockemonList)):
                showPockemon(computerPockemonList[i])
                print()
            
            # getting the results of chosen parameter
            userResult = userCard[userParamChoise]
            compResult = computerCard[userParamChoise]

            # compare results and getting score
            if userResult > compResult:
                userScore += 1
                showResults(computerCard, userParamChoise, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                showResults(computerCard, userParamChoise, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                showResults(computerCard, userParamChoise, userResult, compResult)
                print(f'Equal! The score is: {userScore}/{computerScore}')

        else:
            # getting the pockemons for user and computer
            userPockemon = getPockemon(chosePockemon())
            compPockemon = getPockemon(chosePockemon())
            print()

            # show user's pockemon card
            print(f'Your pockemon: ')
            showPockemon(userPockemon)
            userParamChoise = input('Choose parameter:(id, height, weight) ')
            print()

            # getting values of chosen parameter for user and computer 
            userResult = userPockemon[userParamChoise]
            compResult = compPockemon[userParamChoise]

            # compare results
            if userResult > compResult:
                userScore += 1
                showResults(compPockemon, userParamChoise, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                showResults(compPockemon, userParamChoise, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                print(f'Equal! The score is: {userScore}/{computerScore}')

    else:
        # show the final score after ending the game
        print(f'The final score is: {userScore}/{computerScore}\nGoodbye!')
