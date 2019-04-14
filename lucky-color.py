import random

def guess_lucky_color():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black', 'white']
    lucky_color = random.choice(colors)

    for i in range(3):
        print('The possible colors are {}.'.format(colors))
        guess = input('Guess your lucky color: ')
        if guess == lucky_color:
            print('\nContratulations, you guessed your lucky color!')
            break
        else:
            if i < 2:
                print('\nGuess again!')
                if colors.count(guess) >= 1:
                    colors.remove(guess)
            else:
                print('\nYou\'re out of guesses! The lucky color is {}!'.format(lucky_color))

guess_lucky_color()
