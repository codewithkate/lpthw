# break words
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# sort words
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# print the first word
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# print the last word
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)

# sort a full sentence
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# print the first and last words
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# sort and print the first and last words
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

