the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
boolean = [True,False,False]
dimensional = [[1,2,3],[4,5,6]]

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists (lists of numbers and strings) too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = range(6)

# then use the range function to do 0 to 5 counts (commented out because simplified)
#for i in range (0,6):
#    print(f"Adding {i} to the list.")
    # append is a function that lists understand
#    elements.append(i)

# now we can print them out too.
for i in elements:
    print(f"Element was: {i}")

# use len for total of items in a list
print("This is the length of fruits:",len(fruits))

# identifies the data type. we are obvi working with lists here so what will it print?
print(type(boolean))

# another way to create a list
kate = list(("teacher","american","happy"))
print(kate)

print(dimensional)