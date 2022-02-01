
def is_alphabetical(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    first_letters = []

    for word in sentence:
        first_letters.append(word[0])

    if ''.join(first_letters) in alphabet:
        return "This sentence is alphabetical!"

    else:
        return "This sentence is not alphabetical!"

def is_capitalized(base_string):
    if ''.join(base_string).isupper():
        return "This sentence is capitalized!"

    else:
        return "This sentence is not capitalized!"

def is_alphanumeric(base_string):
    contains_letters = False
    contains_numbers = False
    for char in base_string:
        if isinstance(char, str):
            contains_letters = True

        if char.isnumeric():
            contains_numbers = True

        if contains_letters and contains_numbers:
            return "This sentence is alphanumeric!"

    if contains_letters == False or contains_numbers == False:
        return "This sentence is not alphanumeric!"

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
    if len(''.join(base_string).strip()) == 0:
        break
    print('\n' + is_alphabetical(sentence), '\n')
    print(is_capitalized(sentence), '\n')
    print(is_alphanumeric(base_string), '\n')
    print(lower_to_upper(base_string), '\n')
    print(upper_to_lower(base_string), '\n')
    print(s_to_j(base_string), '\n')

