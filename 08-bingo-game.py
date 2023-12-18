#Bingo Game
#created by Gizelle Alarcon
#Student Number 20210438


print("+---------------------+")
print("|  Welcome to BINGO!  |")
print("+---------------------+\n")

## Defined function to ensure user will key in numbers only.
## inputNumber: function defined
## while True: ensures the loop continues until correct input is keyed
## try: exception to catch
## except ValueError: exception raised
## else: executed when there is no exceptions raised
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("String not accepted, try again")
        else:
            return userInput

## Array of numbers for bingo
bn = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
allbn = len(bn)

## While loop: keeps repeating until quantity within the array is under 0
## Print shows the user what numbers are remaining in their bingo card
## inputnumber variable takes the loop to a function defined above and asks for user input
## if loop: gives directions that if the number entered is within the array to: -
## 1. Remove the number entered from the array.
## 2. Change the total length of the array
## 3. Advise the user that the number is within the list
## else: if number is not within the the array, a print will warn the user that the number is not in their card.
while allbn > 0:
    print("Bingo card numbers:", bn, "\n")
    k = inputNumber("Please key in the numbers drawn: ")

    if k in bn:
        bn.remove(k)
        allbn = len(bn)
        print("Yes! that number is in your list")

    else:
        print("Sorry, that number is not in your list")

## Prints all numbers and congratulates the player
print("+------------------------+")
print("|    CONGRATULATIONS!    |")
print("+----+----+----+----+----+")
print("|  B | I  | N  | G  | O! |")
print("+----+----+----+----+----+")
print("|  7 | 26 | 40 | 58 | 73 |")
print("+----+----+----+----+----+")
print("| 14 | 22 | 34 | 55 | 68 |")
print("+----+----+----+----+----+")
print("|   COLLECT YOUR PRIZE!  |")
print("+------------------------+\n")

'''
Attempt #2
print("+---------------------+")
print("|  Welcome to BINGO!  |")
print("+---------------------+\n")

bn = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
allbn = len(bn)

while allbn > 0:
    print("Your bingo card numbers are:\n", bn, "\n")
    k = int(input("Please key in the numbers called: "))

    if k in bn:
        bn.remove(k)
        allbn = len(bn)
        print("Yes! that number is in your list")

    else:
        print("Sorry, that number is not in your list")

print("BINGO! Collect your prize!")
'''

'''
Attempt #1
BINGO numbers are:
7   26  40  58  73
14  22  34  55  68

bingonumbers = [7, 26]
allbingo = len(bingonumbers)

while allbingo > 0:
    guess = int(input("Guess a number between 1 and 80: "))

    if guess in bingonumbers:
        print("Correct!")
        bingonumbers.remove(guess)
        allbingo = len(bingonumbers)

    else:
        print("Wrong, guess again."))

if allbingo == 0:
    print("Bingo!")

bingonumbers = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]

guess = int(input("Guess a number between 1 and 80: "))
bingonumbers.remove(guess)

while bingonumbers > [0]:
    guess = int(input("Correct! Guess again: "))
    bingonumbers.remove(guess)

print("Bingo!")
'''