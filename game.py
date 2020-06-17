steps = 0
gameOverCondition = False
option = ""


name = input("Enter your name you pillock: ")
print(f" Welcome {name} lets get ready to go on a quest\n you find yourself next haunted house with treasure HAHA!.\n Can you find your way to the treasure?")

response = input(" Are you down to get rich? \n yes or no \n")
if response == "yes" or "y" or "YES" or "Y":
    print(f"\nWelcome through the front door. you can expect to see loads of spider There are 4 room to look for treasure, make your way to your chosen room by using following commands:\n\tk = kitchen\n\th = hallway\n\tl = living room\n\tu = utility")
elif response == "no":
    print("Why you scared? Sorry you aint ready")
    exit()
else:
    print("I don't understand")
    exit()
print("You have 5 chances")

while gameOverCondition == False:
    selection = option
    if option=="":
        selection = input("Enter a room: ")
    if option != "l" or option != "k" or option != "u" or option != "h":
        option = ""
    
    if selection=="k":
        print(f"\nwelcome to the kitchen {name}. Now you have two options \n\tOption 1: Select an item to look under treasure\n\t\tf = Fridge\n\t\to = oven\n\t\tm = microwave \n\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        print(steps)
        option = input("\tpick an option: ")
        if option == "f":
            print("The fridge has lots of dead animals in it now you are surrounded by snakes")
            gameOverCondition = True
        if option == "m":
            print("burnt!! damn thoose microwaves killed you")
            gameOverCondition = True
        if option == "o":
            print("Try again the oven is on you can't open it")
        
    
    if selection == "u":
        print(f"\nwelcome to the Utility room {name}. Now you have two options \n\tOption 1: Select an item to look under treasure\n\t\tb = Bin\n\t\tw = Washing machine\n\t\tc = Cupboard \n\tOption 2: change the room by selecting room option from welcome instrucitions")
        print(steps)
        option = input("\tpick an option: ")
        if option == "b":
            print("You have snake sthat are coming out and you have benn biten")
            gameOverCondition = True
        if option == "c":
            print("Spiders are all of you bye")
            gameOverCondition = True
        if option == "w":
            print("Try again Washing machine is running")
        
            
    
    if selection == "h":
        print(f"\nwelcome to the Hallway {name}. Now you have two options \n\tOption 1: Select an item to look under treasure\n\t\ts = storage cupboard\n\t\tsc = shoe cupboard\n\t\tstr = stairs \n\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        print(steps)
        option = input("\tpick an option: ")
        if option == "s":
            print("You got attacked by a bear hinding in the cupboard")
            gameOverCondition = True
        if option =="sc":
            print("Damn there are to many bats and corono here bye")
            gameOverCondition = True
        if option == "str":
            print("Try again you cannot go upstairs")
            
    
    if selection == "l":
        print(f"\nwelcome to the Living room {name}. Now you have two options \n\tOption 1: Select an item to look under treasure\n\t\ts = Sofa\n\t\tt = TV\n\t\tw = Window \n\tOption 2: change the room by selecting room option from welcome instrucitions")
        steps += 1
        print(steps)
        option = input("\tpick an option: ")
        if option == "s":
            print("You found the coin which is priceless well done for the win!!!!")
            gameOverCondition = True
        if option =="w":
            print("Get out of here bye")
            gameOverCondition = True
        if option == "t":
            print("Try again you cannot do anything with a TV")
            
    if steps == 5:
        print("You had to many chances bye")
        gameOverCondition = True