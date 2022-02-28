# There are [10] different types of people
types_of_people = 10
# The variable x replaces the text giving the value for types_of_people in the string
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# prints the strings from lines 4 and 9
print(x)
print(y)

# repeats the strings from lines 4 and 9
print(f"I said:{x}")
print(f"I also said '{y}'")

# sets the value for hilarious as False and the string for joke_evaluation
hilarious = True
joke_evaluation = ("Isn't that joke so funny?! {}")

print(joke_evaluation.format(hilarious))

# creates values for another joke
w = "This is the left side of..."
e = "a string with a right side."

# prints joke
print(w + e)
