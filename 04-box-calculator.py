# Box Calculator
## Created by Gizelle Alarcon
## Student Number 20210438

print("+---------------------------+")
print("| Welcome to Box Calculator |")
print("+---------------------------+")

## box    is the variable
## int    specifies that the user input is an integer
## input  allows interaction with the user
## ""     text prompting user to key in item quantity
box = int(input("How many items do you have?. Only items more than 5 is accepted: "))

while

#calculation for large box whole number divided by 5
##lb      large box variable
##int     specifies that the output must be a whole number
#box      variable for user input
lb = int(box / 5)

#calculation for medium box remainder divided by 3
##mb      medium box variable
##int     specifies that the output must be a whole number
#box      variable for user input
mb = int(box % 5 / 3)

#calculation for small box remainder from large and medium box divided by 1
##sb      small box variable
##int     specifies that the output must be a whole number
#box      variable for user input
sb = int(box % 5 % 3 / 1)


##print output
print("Thanks for your input \n")

print("You will require: \n")
print("> Large box: ", (lb))
print("> Medium box: ", (mb))
print("> Small box: ", (sb), "\n")


'''
# Code shortened.
print("\n Large box required:", int(box / 5), "\n", "Medium box required:", int(box % 5/ 3), "\n", "Small box required:", int(box % 5 % 4 / 1), "\n")
'''