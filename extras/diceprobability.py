import numpy as np
from collections import Counter

dice = np.random.choice(12, 5, replace=True)

def most_frequent(inp_list):
    """ Returns the most frequent element and number of reccurencies. """
    occurence_count = Counter(inp_list)
    element = occurence_count.most_common(1)[0][0]
    counter = 0
    for i in inp_list:
        if i == element:
            counter+=1
    return element, counter

def throw_again(inp_list):
    """ Throws another throw based on how many recurred dice there are. """
    element, counter = most_frequent(inp_list)
    throw = np.random.choice(12, 5-counter, replace=True)
    for i in throw:
        if i == element:
            counter+=1
    return throw, counter, element

def update(inp_list):
    """ Updates the list of dice with a new throw as well as a new
        counter and element. """
    _,counter = most_frequent(inp_list)
    throw, _, element = throw_again(inp_list)
    update_dice = throw
    i = 0
    while i < counter:
        i+=1
        update_dice = np.append(update_dice, element)
    element, counter = most_frequent(update_dice)
    return throw, update_dice, counter, element

throw2, update_dice, counter, element = update(dice)

throw3, update_dice2, counter2, element2 = update(update_dice)

assert len(dice) == 5
assert len(update_dice) == 5
assert len(update_dice2) == 5

"""
if counter == 5:
    print("Yatzy!")
else:
    print("1st: " + str(dice))
    print("Saves " + str((most_frequent(dice)[1])) + " occurencies of element " \
     + str((most_frequent(dice)[0])))
    print("2nd: " + str(throw2))
    print("New: " + str(update_dice))
    print("3rd: " + str(throw3))
    print("New: " + str(update_dice2))
    print("Element " + str(element2)+ " occured " + str(counter2) + " times.")
"""

yatzies = 0
for i in range(10**4):
    dice = np.random.choice(12, 5, replace=True)
    throw2, update_dice, counter, element = update(dice)
    throw3, update_dice2, counter2, element2 = update(update_dice)
    if counter2 == 5:
        yatzies +=1

print(yatzies)
