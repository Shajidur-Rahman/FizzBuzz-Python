while True:
    try:
        ask = input('Enter a number: ')
        print('Press q to quite: ')
        ask = ask.lower()
        if ask == "q":
            break
        ask = int(ask)
        if (ask % 3) == 0 and (ask % 5) == 0:
            print("Fizz Buzz !! :}")
        elif (ask % 3) == 0:
            print('Fizz !! :)')
        elif (ask % 5) == 0:
            print('Buzz !! :)')
        else:
            print(f'{ask} :( \n Try other numbers')
    except Exception as error:
        print(f'press only "q" and numbers\nThe error is {error}')
print('Thanks for playing the game')


"""
The game is made by Shaidur Rahman
email: shaidurrahmansaad@gmail.com
github: github.com/Shajidur-Rahman/
Thanks for visiting my code.
"""