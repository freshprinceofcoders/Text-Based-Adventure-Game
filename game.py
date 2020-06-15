steps = 0
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

while gameOverCondition == False:
    if option=="":
        selection = input("Enter a room: ")
    if option != "":
        selection == "k"
    if selection=="k":
        print("\nwelcome to the kitchen. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\tf = Fridge\n\t\to = oven\n\t\tm = microwave")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        option = input("\tpick an option: ")
       # selection = option
        if option == "f":
            print("no")
            gameOverCondition = True
        if option == "m":
            print("burnt")
            gameOverCondition = True
        if option == "o":
            print("Try again")
            
    
    if selection == "u":
        print("\nwelcome to the Utility room. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\tb = Bin\n\t\tw = Washing machine\n\t\tc = Cupboard")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        option = input("\tpick an option: ")
        #selection = option
        if option == "b":
            print("You have snake sthat are coming out and you have benn biten")
            gameOverCondition = True
        if option == "c":
            print("Spiders are all of you bye")
            gameOverCondition = True
        if option == "w":
            print("Try again Washing machine is running")
    
    if selection == "h":
        print("\nwelcome to the Hallway. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\ts = storage cupboard\n\t\tsc = shoe cupboard\n\t\tstr = stairs")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        option = input("\tpick an option: ")
        #selection = option
        if option == "s":
            print("You got attacked by a bear hinding in the cupboard")
            gameOverCondition = True
        if option =="sc":
            print("Damn there are to many bats and corono here bye")
            gameOverCondition = True
        if option == "str":
            print("Try again you cannot go upstairs")
            
    
    if selection == "l":
        print("\nwelcome to the Living room. Now you have two options")
        print("\tOption 1: Select an item to look under treasure\n\t\ts = Sofa\n\t\tt = TV\n\t\tw = Window")
        print("\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        option = input("\tpick an option: ")
        #selection = option
        if option == "s":
            print("You found the coin which is priceless well done for the win!!!!")
            gameOverCondition = True
        if option =="w":
            print("Get out of here bye")
            gameOverCondition = True
        if option == "t":
            print("Try again")