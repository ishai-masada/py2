
def is_alphabetical(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for idx, word in enumerate(sentence):
        if word[0] != alphabet[idx]:
            return "\nThis sentence is not alphabetical!"
        count += 1

    if count == len(sentence):
        return "\nThis sentence is alphabetical!"

def is_capitalized(sentence):
    count = 0
    check_variable = True
    for word in sentence:
        if check_variable:
            for letter in word:
                if letter.isupper():
                    return "\nThis sentence is not capitalized!"
            count += 1

    if count == len(sentence):
        return "\nThis sentence is capitalized!"

def is_alphanumeric(base_string):
    contains_letters = False
    contains_numbers = False
    for letter in base_string:
        if contains_letters and contains_numbers:
            return "\nThis sentence is alphanumeric!"
        if isinstance(letter, str):
            contains_letters = True
        if isinstance(letter, int):
            contains_numbers = True

    if contains_letters == False or contains_numbers == False:
        return "\nThis sentence is not alphanumeric!"

def lower_to_upper(base_string):
    for idx, letter in enumerate(base_string):
        if letter == ' ' or letter == '"' or letter.isupper():
            continue
        elif letter.islower():
            base_string[idx] = letter.upper()

    base_string = ''.join(base_string)
    return base_string

def upper_to_lower(base_string):
    for idx, letter in enumerate(base_string):
        if letter == ' ' or letter == '"' or letter.islower():
            continue
        elif letter.isupper():
            base_string[idx] = letter.lower()

    base_string = ''.join(base_string)
    return base_string

def s_to_j(base_string):
    for idx, letter in enumerate(base_string):
        if letter == 's':
            base_string[idx] = 'j'
    return ''.join(base_string)

while True:
    base_string = list(input("Type in a sentence here or just hit enter to end the program: "))
    sentence = ''.join(base_string).split()
    if len(base_string) == 0:
        break
    print('\n', is_alphabetical(sentence))
    print('\n', is_capitalized(sentence))
    print('\n', is_alphanumeric(base_string))
    print('\n', lower_to_upper(base_string))
    print('\n', upper_to_lower(base_string))
    print('\n', s_to_j(base_string))

