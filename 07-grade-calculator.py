#  Box Calculator
## Created by Gizelle Alarcon
## Student Number 20210438

## Program Header
## ""   text prompting user to key in item quantity
print("+-------------------------------+")
print("|   Welcome to Box Calculator   |")
print("+-------------------------------+\n")

## print: contains explanation of how the program works
## \n: new line
print("This program divides items larger than 5 into boxes.\nThere are 3 kinds of boxes:\n - Big box fits 5 items\n - Medium box fits 3 items\n - Small box fits 1 item\n")

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
            print("Character keyed not accepted, please try again.")
        else:
            return userInput

## box: variable name
## inputNumber: uses the function defined as inputNumber
box = inputNumber("How many items do you have? ")

## while box < 5: Endless loop to ensure user keys numbers larger than 5
## inputNumber: defined function loop
while box < 5:
        box = inputNumber("Please key in items more than 5: ")

## print: Final output
## box /5: specifying that this is an integer ensures print will be a whole number. box / 5 = item number divided by 5 shows in large box required.
## box %5 /3: specifying that this is an integer ensures print will be a whole number. box %5 / 3 = item number modulus of 5(remainder of 5) divided by 3 shows in medium box required.
## box %5 %3: specifying that this is an integer ensures print will be a whole number. box %5 %3 = item number modulus of 5 modulus of 3 shows in small box required.
print("\n You will need:\n - Big box:", int(box / 5), "\n", "- Medium box:", int(box %5 / 3), "\n", "- Small box:", int(box % 5 % 3), "\n\nThanks for using Box Calculator. Goodbye!\n")

'''
# First attempt

print("Welcome to Box Calculator")

## Explanation of how the program works
print("This program divides items larger than 5 into boxes.")
print("There are 3 kinds of boxes:")
print(" - Big box can fit 5 items") 
print(" - Medium box can fit 3 items")
print(" - Small box can fit 1 item")

## User input
box = int(input("Please key in your item quantity: "))

## 
bigbox = int(box /5)
medbox = int(box %5 /3)
smlbox = int(box %5 %3 /1)

print("Thanks for your input")
print("Big box: ", bigbox)
print("Medium box: ", medbox)
print("Small box: ", smlbox)
'''
