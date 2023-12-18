list = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
bingo = []

guess = int(input("Guess a number between 1 and 80: "))


for guess in list[10]:
    if guess == []:
        guess = int(input("Correct! Guess again: "))
    else:
        guess = int(input("Wrong! Guess again: "))
    list.remove(guess)
    print("Your guess list: ", guess)
    


print("Bingo!")
