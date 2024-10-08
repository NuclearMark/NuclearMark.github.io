#Mark Irwin

#Creates a Title screen for Spaceship Escape text game.
def title_screen():
    print("\t\t\t\t\t\tSPACESHIP ESCAPE!!!\n\
You must search the rooms and gather seven items.\n\
You need all seven items to be able to survive the trip in the escape pod.\n\
Moves:\tNorth, South, East, West\n\
If you are in a room with an item the game will ask if you would like to gather the item from the room,\n\
if you do want to collect the item type Yes, if you do not simply type No.\n\
Once you have chosen to collect or not to collect an item enter a direction to move to the next room.\n\
Remember though, you need all SEVEN items to survive and win. \n\
Forcing the escape pod to launch will end the game in a defeat.")

    print('-' * 103)
    input("\t\t\t\t\tPlease press enter to start the game!")

#This dictionary links rooms to other rooms while also assigning items that are found within each room.
rooms = {
        'Observatory': {'West': 'Personal Room'},
        'Personal Room': {'West': 'Water Facility', 'East': 'Observatory', 'item': 'Pictures'},
        'Water Facility': {'North': 'Garden', 'East': 'Personal Room', 'item': 'Water'},
        'Garden': {'North': 'Cafeteria', 'South': 'Water Facility', 'item': 'Seeds'},
        'Cafeteria': {'East': 'Captains Room', 'South': 'Garden', 'item': 'Food'},
        'Captains Room': {'East': 'Space Suit Locker', 'West': 'Cafeteria', 'item': 'Escape Code'},
        'Space Suit Locker': {'South': 'Hallway', 'West': 'Captains Room', 'item': 'Space Suit'},
        'Hallway': {'West': 'Escape Pod', 'North': 'Space Suit Locker', 'item': 'a Lost Puppy!'},
        'Escape Pod': {'East': 'Hallway', 'Launch': 'Launch'},
        'Launch': {'East': 'Escape Pod'}
    }
#Assigns a list with one empty string as its element.
direction = ['']

#Creates a list for the players Inventory.
inventory = []

#Starts the game with a title screen.
title_screen()

#Players starting room and current room.
current_room = 'Observatory'

#Function to check players inventory and output all items the player does not have and the room the item is located in.
def check_inventory():
    output = ""
    #Get room names
    for room in rooms.keys():
        #Gets the second dictionary (directions/items)
        room_properties = rooms[room]
        #Checks if there's an item in the room
        if 'item' in room_properties:
            #Get the name of the item in the room
            item = room_properties['item']
            #Checks length of the output.
            if len(output) == 0:
                output = "Remaining items: " + item + " in " + room
            else:
                output += ", " + item + " in " + room
    print(output)

#Gameplay loop
while True:
    #If item is within the directions it will remove item from the directions output and only output the directions.
    directions = [z for z in rooms[current_room].keys() if z != 'item']
    print('You are currently located within the {}'.format(current_room))
    print('You have the following items within your inventory: {}'.format(inventory))
    print('Enter a direction or enter "Exit" to close the game.')
    print("Some pathways and rooms have been destroyed by the asteroids.\n({}) Is currently the only way to change rooms: ".format(','.join(directions)))
    print('-' * 61)
    direction = input('Enter a direction you would like to move: ').capitalize()
    #If player input is exit then program closes.
    if direction == 'Exit':
        print('Thanks for playing')
        break
    #Checks if players entered direction leads to another room.
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    #If players entered direction does not lead to another room outputs an error message.
    else:
        print('The room you are trying to enter has been destroyed by asteroids. Please choose another direction.')
        continue
    #Checks to see if current room is Launch, if current room is launch end game.
    if current_room == 'Launch':
        print('You have chosen to launch without all items. This sadly will be the end of you. You cannot survive the journey back home.')
        print('GAME OVER!')
        break

    #Checks to see if the current room is escape pod and if the number of items in the players inventory is less then seven.
    if current_room == 'Escape Pod' and len(inventory) < 7:
        print('Time is running out, You have arrived at the Escape room unprepared for the journey ahead.')
        print('Go back and get the items you need to survive, More asteroids are coming hurry!!!')
        #calls the function to check the players inventory.
        check_inventory()
    #Checks to see if there is an item in the room the player is currently in.
    if 'item' in rooms[current_room]:
        #Checks to make sure that there is an item in the room but that the item is not already in players inventory.
        if ('item' in rooms[current_room]) and (rooms[current_room]['item'] not in inventory):
            current_item = rooms[current_room]['item']
            print('Somnething you need is in this room!', current_item)
            x = input('Would you like to gather what you need? Yes or No ').capitalize()
            if x == 'Yes':
                #Adds item to players inventory.
                inventory.append(current_item)
    #Checks to see if player is currently in the escape pod and if they have seven items. If so game ends due to player victory.
    if current_room == 'Escape Pod' and len(inventory) == 7:
        print('You have made it to the escape pod and have all items needed to survive.')
        print('You have Survived!')
        #This just makes a puppy display message for fun.
        print('               __')
        print("              /\/'-,")
        print('      ,--\'\'\'\'\'\'\'\'/\"\'')
        print(' ____,\'\')  ) puppy \\___')
        print('"""""""------\'"""`-----\'')
        break