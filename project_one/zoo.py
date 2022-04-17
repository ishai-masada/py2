# Project One
# Zoo program

import pandas

# TODO implement a line plot for tracking the funds over the seven days and count attribute

class Animal:
    def __repr__(self):
        return self.name

    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count

    def animal_earnings(self):
        return (self.cost / 100) * self.count * TICKET_COST

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
        self.display(funds)
        while True:
            if len(self.AVAILABLE_ANIMALS) == 0:
                print("\nThere are no more animals to purchase")
                return

            animal_name = input("\nType in the name of the animal you would like to purchase or nothing to finish: ").strip()

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

                # Check if the user has one of the animals that they want to purchase
                if desired_animal not in self.owned_animals:
                    # Insert the desired animal into the user's collection of animals
                    self.owned_animals[desired_animal.name] = desired_animal

                # Increment the count by one
                self.owned_animals.get(desired_animal.name).count += 1

                print(f"\nYou purchased a {desired_animal.name}!")
                self.display(funds)
            else:
                print("\nYou cannot afford that animal")
                print(f"Your funds: {funds}")

        return funds

    def display(self, funds):
        print(f"\n\"{repr(self)}\"")
        print(f"\nYour budget: {funds}")
        print("\nThese are the animals you can purchase: ")

        for animal in self.AVAILABLE_ANIMALS:
            print(animal, " - $" + str(animal.cost))

        print("\nOwned animals: ")
        if len(self.owned_animals) > 0:
            for animal in self.owned_animals.values():
                print(animal, "(x" + f"{animal.count})", " - $" + str(animal.cost))
        else:
            print("(None)")

    def zoo_earnings(self, funds):
        earnings = 0
        for animal in self.owned_animals:
            earnings += self.owned_animals[animal].animal_earnings()

        funds += earnings

        return funds, earnings

def get_choice():
    print("\nThese are your options: ")
    print("1. Purchase Animals")
    print("2. Calculate earnings and move to the next day")

    while True:
        choice = input("Enter the corresponding number to the option you wish to choose: ").strip()
        if choice.isnumeric() == False:
            print("That was not a valid input.")
        else:
            break

    return choice

TICKET_COST = 50
funds = 10000

zoo = Zoo("St Albans Zoo", {})

for i in range(0, 7):
    print(f'\nDay {i + 1}')

    while True:
        choice = get_choice()

        if choice == '1':
            funds = zoo.purchase_animals(funds)
            continue

        elif choice == '2':
            funds, earnings = zoo.zoo_earnings(funds)
            print(f'\nEarnings for the week: ${earnings}')
            print(f'\nTotal funds: ${funds}')
            break

        else:
            print("\nYour input was not valid.")

