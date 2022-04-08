# Project One
# Zoo program

# TODO Change the way the animals are stored. Add in multiples of the same animal

class Zoo:

    AVAILABLE_ANIMALS = {"Tiger": 7500, "Lion": 15000, "Bear": 15000, "Monkey": 3500,
                         "Giraffe": 60000, "Zebra": 4000, "Rhino": 27000, "Crocodile": 1100,
                         "Whale Shark": 500000, "Turtle": 1000, "Eel": 500,
                         "Reef Shark": 6000, "Starfish": 100, "Manta Ray": 500}

    def __repr__(self):
        return self.name

    def __init__(self, name, owned_animals, funds, daily_rate):
        self.name = name
        self.owned_animals = owned_animals
        self.daily_rate = daily_rate
        self.funds = funds

    def purchase_animals(self):
        self.display()
        while True:
            if len(self.AVAILABLE_ANIMALS) == 0:
                print("\nThere are no more animals to purchase")
                return

            animal_name = input("\nType in the name of the animal you would like to purchase or nothing to cancel: ")

            if len(animal_name) == 0:
                break;

            if animal_name not in self.AVAILABLE_ANIMALS:
                print("\nThat is not an available animal.")
                continue

            animal_cost = self.AVAILABLE_ANIMALS[animal_name]

            if self.funds - animal_cost >= 0:
                self.funds -= animal_cost
                self.owned_animals[animal_name] = animal_cost
                self.AVAILABLE_ANIMALS.get(animal_name)
                print(f"\nYou purchased a {animal_name}!")
                self.display()
            else:
                print("\nYou cannot afford that animal")
                print(f"Your funds: {self.funds}")

    def get_funds():
        pass

    def display(self):
        print(f"\n\"{repr(self)}\"")
        print("\nThese are the animals you can purchase: ")

        for animal in self.AVAILABLE_ANIMALS:
            print(animal, " - $" + str(self.AVAILABLE_ANIMALS[animal]))

        print("\nOwned animals: ")
        if len(self.owned_animals) > 0:
            for animal in self.owned_animals:
                print(animal, " - $" + str(self.owned_animals[animal]))
        else:
            print("(None)")

TICKET_COST = 50

# st_albans_zoo = Zoo("St Albans Zoo", {}, 0, 0)
# franklin_county_zoo = Zoo("Franking County Zoo", {}, 1000000, 0)
# vermont_aquarium = Zoo("Vermont Aquarium", {}, 0, 0)

zoos = [Zoo("St Albans Zoo", {}, 1000000, 0), Zoo("Franking County Zoo", {}, 1000000, 0),
        Zoo("Vermont Aquarium", {}, 1000000, 0)]

for zoo in zoos:
    zoo.purchase_animals()

