# input must be a function already built into the system
# input tells the program to grab whatever is input by the user for the changes
# end='' makes the end of the string a space. you can also place other values between the ''
print("How old are you?", end='')
age = int(input())
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = float(input())

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# add an if statement
print("Do you mind if I ask you a few more questions?",end='')
answer = input()

print("Where do you live?",end='')
live = input()
print("Where are you from?", end='')
origin = input()
print("What languages do you speak?", end='')
languages = (input())

print(f"So, you live in {live}, are from {origin}, and speak {languages}.")

print("One last question?", end='')
okay = input()

print("What does it mean to be human?", end='')
human = input()
print("Thank you for your input, human.")
