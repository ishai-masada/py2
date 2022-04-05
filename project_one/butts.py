# Project One
# Zoo program

def purchase_animals(animals, user_animals, budget):
    while True:
        animal_name = input("\nType in the name of the animal you would like to purchase or nothing to cancel: ")

        if len(animal_name) == 0:
            break;


        if animal_name not in animals:
            print("\nThat is not an available animal.")
            continue

        animal_cost = animals[animal_name]

        if budget - animal_cost >= 0:
            budget -= animal_cost
            user_animals[animal_name] = animal_cost
            available_animals.pop(animal_name)
            print(f"\nYou purchased a {animal_name}!")
            display_animals(available_animals, user_animals)
        else:
            print("\nYou cannot afford that animal")
            print(f"Your budget: {budget}")

def display(available_animals, user_animals, budget):
    print("\nThese are the animals you can purchase: ")
    for animal in available_animals:
        print(animal, " - ", available_animals[animal])

    print("\nYour animals: ")
    if len(user_animals) > 0:
        for animal in user_animals:
            print(animal, " - ", user_animals[animal])
    else:
        print("(None)")

available_animals = {"Tiger": 7500, "Lion": 15000, "Bear": 15000, "Monkey": 3500,
           "Giraffe": 60000, "Zebra": 4000, "Rhino": 27000, "Crocodile": 1100}

user_animals = {}

budget = 100000000

display(available_animals, user_animals, budget)

purchase_animals(available_animals, user_animals, budget)

