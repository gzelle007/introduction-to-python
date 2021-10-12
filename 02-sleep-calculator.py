# Sleep Calculator
# The program must display a welcome message, then prompt the user 
# to enter their year of birth. The program must then calculate and 
# display the number of hours the user has slept in total.

# Prompt user to enter year of birth
user_YOB = int(input("What year were you born?"))
avg_sleep = int(input("How many hours do you sleep a night on average?"))
print("Thank you, calculating now...")

# Calculation
total_sleep = (2021 - user_YOB)*avg_sleep

# Output
print("You have slept a total of", total_sleep, "in your lifetime")
