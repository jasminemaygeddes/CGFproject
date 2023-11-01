print("Welcome to the Top Trumps Game!")
gameMenu = """Game menu:

   1. Pockemon
   2. Harry Potter
   3. Star Wars
   4. Exit
"""

index = False
while index == False:
    print('\n' + gameMenu)

    gameChoice = int(input('Please, choose the option: '))
    if (gameChoice < 1 or gameChoice > 4):
        print('Wrong option')
    elif gameChoice == 1:
        import Pockemon
    elif gameChoice == 2:
        import Harry_Potter
    elif gameChoice == 3:
        import StarWars
    else: 
        index = True
        print('Good Bye!')
