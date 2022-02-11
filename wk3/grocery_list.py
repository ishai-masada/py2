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
# Update:           None
#
#####################################################################################

# Hard-coded grocery list
GROCERY_LIST = {'Granola': 4.50, 'Milk': 3.00, 'Ground Beef': 8.00,
                'Ice Cream': 4.00}

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
    print("\n- Type \"Exit\" to Exit")


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
    item_cost = float(input("Type in the item cost: "))
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
def go_shopping(GROCERY_LIST):
    print('\nItems:\n')
    for item_name in GROCERY_LIST.keys():
        print('-', item_name)
    total_cost = sum(GROCERY_LIST.values())
    print(f'\nTotal Cost: ${total_cost}')

while True:

    # Store the user's input into a variable
    choice = get_choice()

    # Execute the correct function that corresponds to the user's input
    if choice == 'add':
       add(GROCERY_LIST)

    elif choice == 'delete':
       delete(GROCERY_LIST)

    elif choice == 'print':
       print_list(GROCERY_LIST)

    elif choice == 'go shopping':
       go_shopping(GROCERY_LIST)

    elif choice == 'exit':
       break

    # Checks if the user spelled their input incorrectly
    else:
        print("\nThat was not any of the options. Try again.")
