# args act as the boxes for inputting variables and math to run a script with that prints what is indented below each time it is called
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# calls the function cheese_and_crackers and gives variables that go into the boxes for the final print
print("We can just give the funtion numbers directly:")
cheese_and_crackers(20, 30)

# creates variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# variables from lines 14 and 15 are placed as args for the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# function called and sum of the two args print in the script
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calls function and args are a combo of the variables created in lines 14 and 15 with math ; sum of args print
print("And we can combine the two variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# PRACTICE x10
def clothes(shirts, pants, shoes):
    print(f"I have {shirts} shirts.")
    print(f"I have {pants} pants.")
    print(f"I have {shoes} shoes.")
    print(f"And I love each piece!\n")

shirts = 3
pants = 4
shoes = 2

# first
clothes(shirts, pants, shoes)

# second
clothes(4 + 3, 5 + 8, 9 + 3)

nuna = "yellow"
your = "yellow"
business = "yellow"

# third
clothes(nuna, your, business)

print("shirts:")
tops = input()
print("pants:")
bottoms = input()
print("shoes:")
footwear = input()

# fourth
print("\n") ; clothes(tops, bottoms, footwear)

#fifth
def top(one):
    print("There are {one} tops.")
def bottom(two):
    print("There are {two} bottoms.")
def tennis_shoes(three):
    print("There are {three} tennis shoes.")

one = 1
two = 2
three = 3

clothes(top, bottom, tennis_shoes)

# sixth
print("\n") ; clothes(tops, bottoms, footwear)

# seventh
clothes(your, business, nuna)

# eighth
clothes(shirts * 9, pants * 9, shoes * 9)

# ninth
clothes(7 - 5, 8 - 9, 2 - 3)

# tenth
clothes("yellow", "blue", "red")
