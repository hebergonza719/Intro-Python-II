from src.room import Room
from src.player import Player
from src.item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List of in-game items

game_items = {
    'dagger': Item("Dagger", "a short knife with a pointed and edged blade, used as a weapon")
}

room['outside'].items.append(game_items['dagger'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("What is your hero's name?")

print(f"\n{user_name}, I hope you are ready for Hero's Quest.")
print("\nMay your life be long, and your death be swift.")

print("\n-------------------------------------------------------------------------------------")

print("\nPress 'q' to quit game.")

print("\nPress 'n' to move north.\nPress 'e' to move east.\nPress 's' to move south.\nPress 'w' to move west.")

print("\nYou can also take an item or drop an item.")

new_player = Player(user_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
i = True
while i:
    print("\n-------------------------------------------------------------------------------------")
    print(f"\nYou are in {new_player.current_room.name}, {new_player.current_room.description}")

    if len(new_player.current_room.items) > 0:
        for i in new_player.current_room.items:
            print(f"\nThese are the items in this room:")
            print(f"\t {i.name}")

    action = input("\nWhat would you like to do?")
    action_split = action.split()
    if len(action_split) == 1:
        if action == "q":
            print(f"\n{new_player.name}, thank you for playing. Goodbye!")
            break
        elif action == "n":
            if new_player.current_room.n_to is not None:
                new_player.current_room = new_player.current_room.n_to
            else:
                print("\nI'm sorry! That move is not possible.")
        elif action == "e":
            if new_player.current_room.e_to is not None:
                new_player.current_room = new_player.current_room.e_to
            else:
                print("\nI'm sorry! That move is not possible.")
        elif action == "w":
            if new_player.current_room.w_to is not None:
                new_player.current_room = new_player.current_room.w_to
            else:
                print("\nI'm sorry! That move is not possible.")
        elif action == "s":
            if new_player.current_room.s_to is not None:
                new_player.current_room = new_player.current_room.s_to
            else:
                print("\nI'm sorry! That move is not possible.")
    elif len(action_split) == 2:
        if action_split[0] == "get" or action_split[0] == "take":
            print(action.split())
