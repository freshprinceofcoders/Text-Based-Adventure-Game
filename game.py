gameOverCondition = False
option = ""

name = input("Enter your name you pillock: ")
print(f" Welcome {name} lets get ready to go on a quest\n you find yourself next haunted house with treasure HAHA!.\n Can you find your way to the treasure?")

response = input(" Are you down to get rich? \n yes or no \n")
if response == "yes" or "y" or "YES" or "Y":
    print("\nWelcome through the front door. you can expect to see loads of spider")
    print("There are 4 room to look for treasure, make your way to your chosen room by using following commands:\n\tk = kitchen\n\th = hallway\n\tl = living room\n\tu = utility")
elif response == "no":
    print("Why you scared? Sorry you aint ready")
    exit()
else:
    print("I don't understand")
    exit()

while gameOverCondition==False:
    if option=="":
        selection = input("Enter a room: ")

    if selection=="k":
        print("\nwelcome to the kitchen. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\tf = Fridge\n\t\to = oven\n\t\tm = microwave")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        option = input("\tpick an option: ")
        selection = option
        if option=="f":
            print("Congratulations you found the tresure!")
            gameOverCondition=True
        if option=="o":
            print("You're burned by the heat of the oven...get better and try again.")
            gameOverCondition=True
        if option=="m":
            print("Better luch next time try again.")
       

    if selection=="u":
        print("\nwelcome to the utility. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\tw = Washing machine\n\t\tc = cupboard")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        option = input("\tpick an option: ")
        selection = option

