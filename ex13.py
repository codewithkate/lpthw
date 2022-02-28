# this is an import that adds modules to the script from the Python features set
from sys import argv
# read the WYSS section for how to run this
# argv is the argument variable
# line 6 unpacks argv (remember programming is like packing)
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

x = input()
y = input()
