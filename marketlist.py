inventory = {
    "apple": 3,
    "bread": 2,
    "milk": 1
}

while True:

    print("Welcome to online inventory!")
    choices = input(
        "Please choose one! inventory/search for things/add item/remove item/quit: "
    )

    if choices == "inventory":
        print("Here:", inventory)

    elif choices == "search for things":
        print("No problem")
        thing = input("What do you want?: ")

        if thing in inventory:
            print("You already have that in your inventory")
        else:
            print("Ohoo, you don't have that one")

    elif choices == "add item":
        new = input("What would you like to add?: ")
        quantity = int(input("How many?: "))

        if new in inventory:
            inventory[new] += quantity
            print(inventory)
        else:
            inventory[new] = quantity
            print("New shit added to your inventory:", inventory)

    elif choices == "remove item":
        remove = input("Aight, what do you wanna remove?: ")
        quantity = int(input("How many?: "))

        if remove in inventory:

            if inventory[remove] < quantity:
                print("You don't have enough!")

            else:
                inventory[remove] -= quantity

                if inventory[remove] == 0:
                    del inventory[remove]

                print("Here you go homie:", inventory)

        else:
            print("You don't have that, dumbass:", inventory)

    elif choices == "quit":
        print("Goodbye homie!")
        break

    else:
        print("That's not an option!")