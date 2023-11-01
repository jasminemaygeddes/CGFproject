#functions imported on two lines purely so we don't need to scroll to see them all, would absolutely work on a single line. 
#If it doesn't, i think you might need to replace the squirrels.

from game_functions import getStarwars, Choose_Card, showCards, show_results, findUserPockemon, computerPockemon
from game_functions import checkParameter, defineParameter, checkPockemonNumber

userScore = 0
computerScore = 0
answer = 'y'
greetingMsg = 'Do you want to play?(y/n): '
# start game 
while answer == 'y':
    userAnswer = input(greetingMsg).lower()
    answer = userAnswer
    
    # check user's answer
    if userAnswer == 'y':
        # ask user how many cards he/she wants to play with
        cardNumber = int(input('How many cards do you want to play with?(min: 1; max: 5): '))
        
        # check the quantity of playing cards
        if cardNumber > 1 and cardNumber <= 5:
            # creating empty lists of pockemons for user and computer
            userCardList = []
            computerCardList = []

            # show user's assigned cards
            print('\nYour cards:')
            
            for i in range(cardNumber):
                # fill the user pockemon list and show it to user
                userCardList.append(getStarwars(Choose_Card())) 

                print(f'\nCard number {i + 1}:\n')
                showCards(userCardList[i])

                # fill the computer pockemon list
                computerCardList.append(getStarwars(Choose_Card())) 

            print()

            # get parameters from userCards
            paramStatus = False

            # check the user's input 
            while paramStatus == False:
                userParamChoiceInput = input('Choose parameter: height(h), weight(w) ').lower()
                paramStatus = checkParameter(userParamChoiceInput)
            
            # getting full name of parameter for pockemon's dictionary
            userParamChoice = defineParameter(userParamChoiceInput)

            # check input of chosen pockemon
            status = False 
            while status == False:
                userCardChoice = int(input('Choose the card number: '))
                status = checkPockemonNumber(userCardChoice, cardNumber)
           
            # getting 1 chosen card from user and with max value computer card
            computerCard = computerPockemon(computerCardList, userParamChoice)
            userCard = findUserPockemon(userCardList, userCardChoice - 1)
            print() 

            print(f'You choose: {userCard["name"].upper()}!')
            showCards(userCard)
            print()
            
            # show computer's cards
            print("Your opponent's cards:")
            for i in range(len(computerCardList)):
                showCards(computerCardList[i])
                print()
            
            # getting the results of chosen parameter
            userResult = userCard[userParamChoice]
            compResult = computerCard[userParamChoice]

            if userResult == 'unknown':
                userResult = 0
            
            if compResult == 'unknown':
                compResult = 0
            
            userResult = int(userResult)
            compResult = int(compResult)

            # compare results and getting score
            if userResult > compResult:
                userScore += 1
                show_results(computerCard, userParamChoice, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                show_results(computerCard, userParamChoice, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                show_results(computerCard, userParamChoice, userResult, compResult)
                print(f'Equal! The score is: {userScore}/{computerScore}')

        elif cardNumber == 1:
            # getting the cards for user and computer
            userCards = getStarwars(Choose_Card())
            compCards = getStarwars(Choose_Card())
            print()

            # show user's pockemon card
            print(f'Your card: ')
            showCards(userCards)
            paramStatus = False
            
            # get parameter from user
            # check the input of parameter
            while paramStatus == False:
                userParamChoiceInput = input('Choose parameter: height(h), weight(w) ').lower()
                paramStatus = checkParameter(userParamChoiceInput)
            
            # getting full name of parameter for pockemon's dictionary
            userParamChoice = defineParameter(userParamChoiceInput)
            print()

            # getting values of chosen parameter for user and computer 
            userResult = userCards[userParamChoice]
            compResult = compCards[userParamChoice]

            if userResult == 'unknown':
                userResult = 0

            if compResult == 'unknown':
                compResult = 0
            
            userResult = int(userResult)
            compResult = int(compResult)

            # compare results

            if userResult > compResult:
                userScore += 1
                show_results(compCards, userParamChoice, userResult, compResult)
                print(f'You won! The score is: {userScore}/{computerScore}')

            elif userResult < compResult:
                computerScore += 1
                show_results(compCards, userParamChoice, userResult, compResult)
                print(f'You lose. The score is: {userScore}/{computerScore}')
            else:
                print(f'Draw! The score is: {userScore}/{computerScore}')

        else: 
            print('Check number of cards. Max number of card is 5')

    elif userAnswer == 'n':
        # show the final score after ending the game
        print(f'The final score is: {userScore}/{computerScore}\nGoodbye!')
    else: 
        print('Wrong input\nPlease, choose correct answer (y or n)')
        answer = 'y'



