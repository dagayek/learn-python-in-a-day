import random

prizes = [0,0,0,5,10,25,100]
cash = 100

def lottery_number_game():
    global cash
    while cash >= 10:
        cmd = input('[P]lay or [Q]uit: ')

        if cmd == 'P' or cmd == 'p' or cmd == 'play' or cmd == 'Play':
            lottery_numbers = generate_lottery_numbers()
            num_set = buy_ticket()
            drawing_result(lottery_numbers, num_set)
        elif cmd == 'Q' or cmd == 'q' or cmd == 'Quit' or cmd == 'quit':
            print('Thanks for playing!\n')
            break
        else:
            print('Unrecognized command.\n')

    print('You finished with  ${} remaining.'.format(cash))


def generate_lottery_numbers():
    lottery_numbers = set()

    while len(lottery_numbers) < 6:
        lottery_numbers.add(random.randint(1,20))

    return lottery_numbers

def buy_ticket():
    global cash
    cash -= 10

    num_set = set()
    while len(num_set) < 6:
        nums = input('Enter {} numbers between 0 and 20: '.format(6-len(num_set)))
        nums = nums.replace(',', ' ')
        nums_list = nums.split()
        
        if len(nums_list) > 6-len(num_set):
            print('You entered too many numbers, please try again.\n')
            continue
        
        try:
            num_set = num_set.union(convert_to_set(nums_list))
        except ValueError:
            continue

    return num_set

def drawing_result(lottery_numbers, num_set):
    global cash
    matching_set = num_set.intersection(lottery_numbers)
    result = len(matching_set)

    print('The lottery numbers are: {}'.format(lottery_numbers))
    print('Your numbers are: {}'.format(num_set))
    print('Your matching numbers: {}'.format(matching_set))

    if result <= 2:
        print('Better luck next time! You got {} matches and won {} dollars.\nYou have {} dollars remaining.\n'.
                format(result, prizes[result], cash))
    elif result > 2 or result < 6:
        cash += prizes[result]
        print('Congratulations! You got {} matches and won {} dollars.\nYou have {} dollars remaining.\n'.
                format(result, prizes[result], cash))
    else:
        cash += prizes[result]
        print('Jackpot! You got {} matches and won {} dollars.\nYou have {} dollars remaining.\n'.
                format(result, prizes[result], cash))
        
def convert_to_set(s):
    ret_set = set()
    for n in s:
        try:
            int(n)
        except ValueError:
            print('Invalid input. {} not an integer. Please try again.\n'.format(n))
            raise

        n = int(n)
        if n < 0 or n > 20:
            print('Value {} out of bounds. Please try again.\n'.format(n))
            raise ValueError()
        
        ret_set.add(n)
    return ret_set

lottery_number_game()
