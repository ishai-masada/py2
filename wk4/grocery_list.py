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
    print("\n- Type \"Next\" to go to the next week")


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
# Function Name:  get_name_cost
#
# Date:           2/7/22
#
# Purpose:       Prompts the user for the name of an item and the cost of that item
#
# Who called           N/A
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def get_name_cost():
    items = {}
    while True:
        while True:
            item_name = input("\nType in the name of the item that you want to add to the "
                               "grocery list, or type nothing to finish: ").strip().lower().title()
            try:
                float(item_name)
                int(item_name)
                print("\nYou can only enter letters, not numbers")
                continue

            except:
                break

        if len(item_name) == 0:
            break

        while True:
            cost = input("\nType in the cost of the item or type nothing to cancel: ").strip().lower()
            try:
                float(cost)
                break
            except:
                if cost.isnumeric() == False:
                    print("\nYou can only enter numbers, not letters")
                    continue

        if len(cost) == 0:
            break

        items[item_name] = float(cost)

    return items

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
def add(GROCERY_LIST, week_cost):
    for item_name, cost in get_name_cost().items():
        GROCERY_LIST[item_name] = float(cost)

    week_cost = sum(GROCERY_LIST.values())
    return GROCERY_LIST, week_cost

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
def delete(GROCERY_LIST, week_cost):
    while True:
        if len(GROCERY_LIST) == 0:
            print("\nThe grocery list is empty.")
            break

        item_name = input("Type in the name of the item that you want to delete from the "
                           "grocery list, or type nothing to finish: ").strip().lower().title()
        if len(item_name) == 0:
            break

        GROCERY_LIST.pop(item_name)
    week_cost = sum(GROCERY_LIST.values())

    return GROCERY_LIST, week_cost

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
def get_list(GROCERY_LIST, week_cost):
    GROCERY_LIST.clear()
    for item_name, cost in get_name_cost().items():
        GROCERY_LIST[item_name] = float(cost)

    week_cost = sum(GROCERY_LIST.values())

    return GROCERY_LIST, week_cost

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
    week_cost = round(sum(GROCERY_LIST.values()), 3)
    print(f'\nTotal Cost: ${week_cost}')

total_cost = 0

# Repeat for 4 weeks
GROCERY_LIST = {}

count = 0

for i in range(4):

    week_cost = 0
    GROCERY_LIST, week_cost = get_list(GROCERY_LIST, week_cost)

    # Menu prompt
    while True:

        # Store the user's input into a variable
        choice = get_choice()

        # Execute the correct function that corresponds to the user's input
        if choice == 'next':
            break

        elif choice == 'add':
           GROCERY_LIST, week_cost = add(GROCERY_LIST, week_cost)

        elif choice == 'delete':
           GROCERY_LIST, week_cost = delete(GROCERY_LIST, week_cost)

        elif choice == 'print':
           print_list(GROCERY_LIST)

        elif choice == 'go shopping':
           go_shopping(GROCERY_LIST, week_cost)

        # Check if the user spelled their input incorrectly
        else:
            print("\nThat was not any of the options. Try again.")

    total_cost += week_cost

print(f'\nThis is the total amount of money spent over the 4 weeks: {total_cost}')
