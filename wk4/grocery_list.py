#####################################################################################
#
# Name:   Ishai Masada
#
# Date:
#
# Purpose:  Create a grocery list for shopping
#
# Functions:       None
#
# Update:   Converted any of the code that is not built as a function, to a function.
#           Added a function that allows the user to create a grocery list for 4 weeks,
#           a new one each week.
#
#####################################################################################

#####################################################################################
#
# Function Name:  display
#
# Date:           2/7/22
#
# Purpose:       Displays the menu options to the user
#
# Who called:           get_choice() function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def display():
    print("\n- Type \"Add\" to Add items to the grocery list")
    print("\n- Type \"Delete\" to  Delete items from the grocery list")
    print("\n- Type \"Print\" to Print the grocery list")
    print("\n- Type \"Go shopping\" to Go shopping")
    print("\n- Type \"Skip\" to skip to the next week")


#####################################################################################
#
# Function Name:  get_choice
#
# Date:           2/7/22
#
# Purpose:       Prompts the user to choose what they want to do
#
# Who called           While loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def get_choice():
    print("\nThese are your options: ")
    display()
    choice = input("\nWhat do you wish to do? ").strip().lower()
    return choice

#####################################################################################
#
# Function Name:  add
#
# Date:           2/7/22
#
# Purpose:       Allows the user to add an item to their grocery list
#
# Who called           if statement
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def add(GROCERY_LIST):
    item_name = input("Type in the item name to add: ")
    item_cost = input("Type in the item cost: ")
    GROCERY_LIST[item_name.title()] = item_cost

#####################################################################################
#
# Function Name:  delete
#
# Date:           2/1/22
#
# Purpose:       Allows the user to delete an item to their grocery list
#
# Who called           elif statement
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def delete(GROCERY_LIST):
    item_name = input("Type in the item name to remove: ").strip().lower().title()
    GROCERY_LIST.pop(item_name)

#####################################################################################
#
# Function Name:  print_list
#
# Date:           2/7/22
#
# Purpose:       Prints out the list of items
#
# Who called           elif statement
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def print_list(GROCERY_LIST):
    print()
    for item_name, cost in GROCERY_LIST.items():
        print('-', f'{item_name}:', cost)
    print()

#####################################################################################
#
# Function Name:  get_list
#
# Date:           2/11/22
#
# Purpose:       Prompts the user to create a new grocery list
#
# Who called           TBD
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def get_list(GROCERY_LIST):
    GROCERY_LIST.clear()

    while True:
        item_name = input("Type in the name of the item that you want to add to the "
                           "grocery list, or type nothing to finish: ").strip().lower().title()
        if len(item_name) == 0:
            break

        cost = input("Type in the cost of the item or type nothing to cancel: ").strip().lower()
        if len(cost) == 0:
            break

        GROCERY_LIST[item_name] = cost
    return GROCERY_LIST


#####################################################################################
#
# Function Name:  go_shopping
#
# Date:           2/7/22
#
# Purpose:       Prints out the list of items and calculates the total cost
#
# Who called           elif statement
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def go_shopping(GROCERY_LIST, week_cost):
    print('\nItems purchased:\n')
    for item_name in GROCERY_LIST.keys():
        print('-', item_name)
    print(f'\nTotal Cost: ${week_cost}')
    return total_cost

total_cost = 0

# Repeat for 4 weeks
GROCERY_LIST = {}

count = 0

for i in range(5):

    GROCERY_LIST = get_list(GROCERY_LIST)

    # Menu prompt
    while True:

        week_cost = sum(GROCERY_LIST.values())

        # Store the user's input into a variable
        choice = get_choice()

        # Execute the correct function that corresponds to the user's input
        if choice == 'skip':
            break

        elif choice == 'add':
           add(GROCERY_LIST)

        elif choice == 'delete':
           delete(GROCERY_LIST)

        elif choice == 'print':
           print_list(GROCERY_LIST)

        elif choice == 'go shopping':
           go_shopping(GROCERY_LIST, week_cost)

        # Checks if the user spelled their input incorrectly
        else:
            print("\nThat was not any of the options. Try again.")


print(f'\nThis is the total amount of money spent over the 4 weeks: {total_cost}')
