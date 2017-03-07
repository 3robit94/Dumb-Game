from player import Player
import world
from collections import OrderedDict
from colorama import init, Fore, Back, Style
init()

def play():
	print("						" + Fore.RED + Back.BLUE + Style.BRIGHT + "Escape from Castle Evil!" + Fore.WHITE + Back.BLACK + Style.NORMAL)
	player = Player()
	while True:
		room = world.tileAt(player.x, player.y)
		print(room.introText())
		room.modifyPlayer(player)
		choose_action(room,player)
	
def	getAvailableActions(room, player):
	actions = OrderedDict()
	print("Choose an action: ")
	if player.inventory:
		actionAdder(actions, 'i', player.printInventory, "Show Inventory")
	if isinstance(room, world.EnemyTile) and room.Enemy.isAlive():
		actionAdder(actions, 'a', player.attack, "Attack")
	else:
		if world.tileAt(room.x, room.y - 1):
			actionAdder(actions, 'n', player.moveNorth, "Go north")
		if world.tileAt(room.x, room.y + 1):
			actionAdder(actions, 's', player.moveSouth, "Go south")
		if world.tileAt(room.x + 1, room.y):
			actionAdder(actions, 'e', player.moveEast, "Go east")
		if world.tileAt(room.x - 1, room.y):
			actionAdder(actions, 'w', player.moveWest, "Go west")
	if player.hp < 1000:
		actionAdder(actions, 'h', player.heal, "Heal")
		
	return actions

def actionAdder(actionDict, hotkey, action, name):
	actionDict[hotkey.lower()] = action
	actionDict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

def choose_action(room, player):
	action = None
	while not action:
		availableActions = getAvailableActions(room, player)
		action_input = input("Action: ")
		action = availableActions.get(action_input)
		if action:
			action()
		else:
			print("Invalid action")

play()