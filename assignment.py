import random
import os
import time


def is_valid(coordinate, c_letters, size, opened):
    if len(coordinate) != 2:
        return False
    if coordinate in opened:
        print("You've already opened that card, didn't you? I beg you, stop wasting your time and computer's memory")
        return False
    if not coordinate[0].isdecimal() or int(coordinate[0]) > size or int(coordinate[0]) <= 0:
        return False
    if not coordinate[1].upper() in c_letters:
        print(f"There's no such letter) Please, enter the one available: {c_letters[1:]}s")
        return False
    return True

def process_coordinate(coordinate):
    coordinate[0] = int(coordinate[0]) - 1
    coordinate[1] = (ord(coordinate[1].upper()) - 65)
    return coordinate


#create the needed variables and dictionaries
SIZE = 4
card_values = '!@#$%+&*'
guessed_values = []
opened_cards = []
step_counter = 0

values = [['X']*SIZE for i in range(SIZE)]
values_raw = [['X']*SIZE for i in range(SIZE)]


letters = [chr(i+65) for i in range(SIZE)]
letters.insert(0, chr(32)*2)

#Filled a dictionary with usage of values
used_values = {}
for i in card_values:
    used_values[i] = 0
#Put values into a matrix
for i in card_values:
    while used_values[i] < 2:
        row = random.randrange(0, SIZE)
        column = random.randrange(0, SIZE)
        if values[row][column] == 'X':
            values[row][column] = i
            used_values[i] += 1

print(f'''Welcome to the MEMORIZER game! The rules are simple:
1. You pick up tow cards
2. If the signs are the same, those cards are left open
3. If the signs are different, cards are closing, and you're given another try
4. In the end you'll see your score
5. All the signs you'll have are: {card_values}
Good luck and enjoy!''')

#while playing (while number of stored items =! the whole amount of numbers)
while len(guessed_values) != len(card_values):
    start = time.time()
    #print the table (with stored items)
    for row in range(SIZE):
        if row == 0:
            for letter in letters:
                print(letter, end=' ')
            print()
        print(f'{row+1}.', end=' ')
        for column in range(SIZE):
            if values[row][column] in guessed_values:
                print(values[row][column], end=' ')
            else:
                print(values_raw[row][column], end=' ')
        print()