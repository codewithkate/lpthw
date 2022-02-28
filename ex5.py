# input value for the variable name
name = 'Kate A. Crawford'
# input value for the variable age. do not lie
age = 24
# input value for the variable height
height = 66 #inches
# input value for the variable weight
weight = 140 #lbs
# input value for the variable eyes
eyes = 'Blue'
# input value for the variable teeth
teeth = 'White'
hair = 'Brown'

# convert to the metric system
height = round(height * 2.54)
# input value for the variable hair
weight = round(weight * 0.45359237)

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
