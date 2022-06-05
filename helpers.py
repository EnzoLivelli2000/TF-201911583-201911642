import random

# This function generate a random color 
def random_color():
    colorRandom = "#"
    letters = ['a', 'b', 'c', 'd', 'e']
    for i in range(6):
        option = random.randint(1,2)
        if option == 1: # Generate a random number between 0-9
            colorRandom += str(random.randint(0,9))
        else:
            numberPosition = random.randint(0,4)
            colorRandom += letters[numberPosition]
    return colorRandom

