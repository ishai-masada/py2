# Project One
# Zoo program

# Import matplotlib
import matplotlib.pyplot as plot

# Import numpy
import numpy

# Animal Class
class Animal:
    # Define the repr
    def __repr__(self):

        # Return the instance's name
        return self.name

    # Define the constructor
    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count

    # Define the earnings method
    def animal_earnings(self):
        # Returns the estimated amount of funds earned in a day
        return (self.cost / 100) * self.count * TICKET_COST

# Zoo Class
class Zoo:

    # Available animals of Animal Class type class variable for user to choose from
    AVAILABLE_ANIMALS = [Animal("Tiger", 7500, 0), Animal("Lion", 15000, 0),
                         Animal("Bear", 15000, 0), Animal("Monkey", 3500, 0),
                         Animal("Giraffe", 60000, 0), Animal("Zebra", 4000, 0),
                         Animal("Rhino", 27000, 0), Animal("Crocodile", 1100, 0),
                         Animal("Whale Shark", 500000, 0), Animal("Turtle", 1000, 0),
                         Animal("Eel", 500, 0), Animal("Reef Shark", 6000, 0),
                         Animal("Starfish", 100, 0), Animal("Manta Ray", 500, 0)
                        ]

    # Define the repr
    def __repr__(self):
        return self.name

    # Define the constructor
    def __init__(self, name, owned_animals):
        self.name = name
        self.owned_animals = owned_animals

    # Define the animal purchasing method
    def purchase_animals(self, funds):
        # Call the display Zoo method
        self.display(funds)

        # Inifinite Loop
        while True:

            # Prompt the user to enter the name of the animal that they want to purchase
            animal_name = input("\nType in the name of the animal you would like to purchase or enter to finish: ").strip().title()

            # Check if the user entered nothing
            if len(animal_name) == 0:
                break;

            # Check if the animal name is valid
            desired_animal = None

            # Iterate over the available animals
            for animal in self.AVAILABLE_ANIMALS:

                # Check if the name is an available name
                if animal_name == animal.name:
                    desired_animal = animal
                    break

            # Check if the user entered a valid name
            if desired_animal == None:
                print("\nThat is not an available animal.")
                continue

            # Check if the can afford to purchase the desired animal
            if funds - desired_animal.cost >= 0:

                # Decrement their funds by the cost of the desired animal
                funds -= desired_animal.cost

                # Check if the user has one of the animals that they want to purchase
                if desired_animal not in self.owned_animals:

                    # Insert the desired animal into the user's collection of animals
                    self.owned_animals[desired_animal.name] = desired_animal

                # Increment the count by one
                self.owned_animals.get(desired_animal.name).count += 1

                print(f"\nYou purchased a {desired_animal.name}!")

                # Call the display Zoo Class method
                self.display(funds)

            else:
                print("\nYou cannot afford that animal")
                print(f"Your funds: {funds}")

        return funds

    # Define the display Zoo Class method
    def display(self, funds):
        print(f"\n\"{repr(self)}\"")
        print(f"\nYour budget: {funds}")
        print("\nThese are the animals you can purchase: ")

        # Iterate over the available animals
        for animal in self.AVAILABLE_ANIMALS:

            # Print each animal's name and cost
            print(animal, " - $" + str(animal.cost))

        print("\nOwned animals: ")

        # Check if the user has any animals
        if len(self.owned_animals) > 0:

            # Iterate over the user's animals
            for animal in self.owned_animals.values():

                # Print each animal's name and cost
                print(animal, "(x" + f"{animal.count})", " - $" + str(animal.cost))
        else:
            print("(None)")

    # Define the earnings Zoo Class method
    def zoo_earnings(self, funds, graph_input, day):
        earnings = 0

        # Get all of the earnings from each owned animal
        for animal in self.owned_animals:
            earnings += self.owned_animals[animal].animal_earnings()

        # Calculate the total funds given the week's earnings
        funds += earnings

        # Add the current amount of funds to the input data for the graph
        graph_input["Day"].append(day+1)
        graph_input["Funds"].append(funds)

        # Set up the arrays of data for the graph
        x_values = numpy.array(graph_input["Day"])
        y_values = numpy.array(graph_input["Funds"])

        # Create the plot for the graph using the graph input data
        plot.plot(x_values, y_values)

        # Add axis labels and a title
        plot.title("Your Funds")
        plot.xlabel("Day")
        plot.ylabel("Amount")

        # Display the scatter plot
        plot.show()

        return funds, earnings, graph_input

# Define the get choice function
def get_choice():
    print("\nThese are your options: ")
    print("1. Purchase Animals")
    print("2. Calculate earnings and move to the next day")

    # Infinite Loop
    while True:

        # Prompt the user to enter the number of the option they want to do
        choice = input("Enter the corresponding number to the option you wish to choose: ").strip()

        # Check if they didn't enter a number
        if choice.isnumeric() == False:
            print("That was not a valid input.")
        else:
            break

    return choice

TICKET_COST = 50
funds = 10000

# Initialize the Zoo object
zoo = Zoo("St Albans Zoo", {})

# Initialize the graph input
graph_input = {"Day": [0],
               "Funds": [0]}
day = 0

# Conditional Loop
while day < 7:
    print(f'\nDay {day + 1}')

    # Infinite Loop
    while True:
        choice = get_choice()

        # Check if the user entered a 1
        if choice == '1':

            # Get the user's total funds
            funds = zoo.purchase_animals(funds)
            continue

        # Check if the user entered a 2
        elif choice == '2':

            # Calculate the user's funds and earnings for the day
            funds, earnings, graph_input = zoo.zoo_earnings(funds, graph_input, day)
            print(f'\nEarnings for the day: ${earnings}')
            print(f'\nTotal funds: ${funds}')
            break

        else:
            print("\nYour input was not valid.")
    day += 1

# Calcualte the user's profits for the week
profit = funds - 10000

# Check if the user has earned profit
if profit > 0:
    print(f'\nYou earned ${profit} in profits!')

# Check if the user did not make a profit
elif profit == 0:
    print(f'\nYou earned zero profit!')

# Check if the user lost money
elif profit < 0:
    print(f'\nYou lost {abs(profit)}!')
