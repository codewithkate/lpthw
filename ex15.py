from sys import argv

# what is needed to run the script
script, filename = argv

# stores the contents from filename
txt = open(filename)

# reads the txt from filename
print(f"Here's your file {filename}: ")
print(txt.read())
