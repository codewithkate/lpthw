# new variable called formatter
formatter = "{}{}{}{}"

# the first input for {1} is 1, 2, 3, 4
print(formatter.format(1, 2, 3, 4))
# the second input for {2} is "one", "two", "three", "four"
print(formatter.format("one", "two", "three", "four"))
# the third input for {3} is True, False, False, True
print(formatter.format(True, False, False, True))
# the fourth input for {4} is "{}{}{}{}" * 4
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Today",
" / Right here, Right now",
" / We'll love again",
" / We've already found someone <3"
))
