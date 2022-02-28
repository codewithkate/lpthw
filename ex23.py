# command line arguemnt: you'll need to call the script, codec and error strictness? for this arg
import sys
script,encoding,error = sys.argv

# create a funtion called main that has the lang file, encoding, and errors with a variable called line that reads a line from the lang file. called at the end of the script.
def main(language_file,encoding,errors):
    line = language_file.readline()
# if statement tests to see if the variable, line, has foudn something while reading the file. If it is true then reads lines 9-10: prints the line, and loops the main function
    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)
# creates function called print_line that encodes each line from the lang file with three new variables (next_lang=strips \n,raw_bytes=contents of file to binary,cooked_string=reverses encoding to human lang?)>>DBES
def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes,"<===>", cooked_string)

# creates variable called languages that opens the lang file and encodes it with utf-8 which is 8bytes or 64 bits
languages = open("languages.txt",encoding="utf-8")

main(languages,encoding,error)
