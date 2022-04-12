# Project One
# Zoo program

import pandas

# TODO implement a line plot for tracking the funds over the seven days

class Animal:
    def __repr__(self):
        return self.name

    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost

    def get_daily_rate(self):
        return self.cost / TICKET_COST

    def calculate_earnings(self):
        return self.count * self.daily_rate(self)

class Zoo:

    AVAILABLE_ANIMALS = [Animal("Tiger", 7500, 0), Animal("Lion", 15000, 0),
                         Animal("Bear", 15000, 0), Animal("Monkey", 3500, 0),
                         Animal("Giraffe", 60000, 0), Animal("Zebra", 4000, 0),
                         Animal("Rhino", 27000, 0), Animal("Crocodile", 1100, 0),
                         Animal("Whale Shark", 500000, 0), Animal("Turtle", 1000, 0),
                         Animal("Eel", 500, 0), Animal("Reef Shark", 6000, 0),
                         Animal("Starfish", 100, 0), Animal("Manta Ray", 500, 0)
                        ]

    def __repr__(self):
        return self.name

    def __init__(self, name, owned_animals):
        self.name = name
        self.owned_animals = owned_animals

    def purchase_animals(self, funds):
        self.display()
        while True:
            if len(self.AVAILABLE_ANIMALS) == 0:
                print("\nThere are no more animals to purchase")
                return

            animal_name = input("\nType in the name of the animal you would like to purchase or nothing to cancel: ")

            if len(animal_name) == 0:
                break;

            # Check if the animal name is valid
            desired_animal = None

            for animal in self.AVAILABLE_ANIMALS:
                if animal_name == animal.name:
                    desired_animal = animal
                    break

            if desired_animal == None:
                print("\nThat is not an available animal.")
                continue

            if funds - desired_animal.cost >= 0:
                funds -= desired_animal.cost
                self.owned_animals.append(desired_animal)
                print(f"\nYou purchased a {desired_animal.name}!")
                self.display()
            else:
                print("\nYou cannot afford that animal")
                print(f"Your funds: {funds}")

    def display(self):
        print(f"\n\"{repr(self)}\"")
        print("\nThese are the animals you can purchase: ")

        for animal in self.AVAILABLE_ANIMALS:
            print(animal, " - $" + str(animal.cost))

        print("\nOwned animals: ")
        if len(self.owned_animals) > 0:
            for animal in self.owned_animals:
                print(animal, " - $" + str(animal.cost))
        else:
            print("(None)")

def get_choice():
    print("\nThese are your options: ")
    print("1. Purchase Animals")
    print("2. Calculate earnings and move to the next day")

    while True:
        choice = input("Enter the corresponding number to the option you wish to choose: ")
        if choice.isnumeric() == False:
            print("That was not a valid input.")
        else:
            break

    return choice

def calculate_earnings():
    pass

TICKET_COST = 50
funds = 10000

zoo = Zoo("St Albans Zoo", [])

for i in range(0, 7):
    print(f'\nDay {i + 1}')

    while True:
        choice = get_choice()

        if choice == '1':
            zoo.purchase_animals(funds)
            continue

        elif choice == '2':
            calculate_earnings()
            break

        else:
            print("\nYour input was not valid.")
