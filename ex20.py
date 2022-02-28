from sys import argv

# needs two files to run
script, input_file = argv

# function named print_all with an arg called f will use the read function to print all of text in f
def print_all(f):
    print(f.read())

# function named rewind will use the seek function within arg f
def rewind(f):
    f.seek(0)

# funciton called print_a_line has two args, line_count and f, that will print the line_count fllowed by reading a line from f using readline function
def print_a_line(line_count, f):
    print(line_count, f.readline())

# creates variable current_file that opens input_file
current_file = open(input_file)

# prints string and creats new line between the next print
print("First let's print the whole file:\n")

# calls print_all function and uses the variable current_file as arg to  open input_file
print_all(current_file)

# prints string
print("Now let's rewind, kind of like a tape.")

# calls the rewind function and uses variable current_file as arg which opens input_file then does the seek function ; 0?
rewind(current_file)

# prints string
print("Let's print three lines:")

# creates variable calles current_file and makes it equal to 1
current_line = 1
# calls print_a_line function that prints current_line (1) as argline_count and current_file as argf
print_a_line(current_line, current_file)

# redefines current_line as 2 by adding 1 to current_line from line 37
current_line = current_line + 1
# prints line count as 2
print_a_line(current_line, current_file)

# redefines current_line as 3 by adding 1 to the current_line from line 42; this is compounding the variable if that's how you would say this
current_line = current_line + 1
# prints line counts as 3
print_a_line(current_line, current_file)
