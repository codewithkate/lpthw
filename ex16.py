# what is sys? still not sure on argv?
from sys import argv

# tells what script to run and the file that this script will write on
script,filename = argv

# prompts user with choice to erase contents of the txt file or to cancel
print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

# prompts with a ?
input("?")

# opens the file but why the 'w'
print("Opening the file...")
target = open(filename,'w')

# truncate means to take off the head of something in this case it also means to wipe clean
print("Truncating the file. Goodbye!")
target.truncate()

print("Now, I'm going to ask you for three lines.")

# user inputs contents fo 3 lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# saves new content to file
print("And finally, we close it.")
target.close()
