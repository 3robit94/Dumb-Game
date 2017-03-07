import items
import world
from colorama import init, Fore, Back, Style
init()

class Player:
	def __init__(self):
		self.inventory = [items.Dagger(), 'Gold(5)', items.MoldyBread(), items.HealingPotion()]
		self.x = 1
		self.y = 2
		self.hp = 1000
		
	def printInventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item))
		
	def mostPowerfulWeapon(self):
		maxDamage = 0
		bestWeapon = None
		for item in self.inventory:
			try:
				if item.damage > maxDamage:
					bestWeapon = item
					maxDamage = item.damage
			except AttributeError:
				pass
		
		return bestWeapon
	
	def attack(self):
		bestWeapon = self.mostPowerfulWeapon()
		room = world.tileAt(self.x,self.y)
		enemy = room.Enemy
		print("You use {} against {}!".format(bestWeapon.name, enemy.name))
		enemy.hp -= bestWeapon.damage
		if not enemy.isAlive():
			print(Fore.RED + Back.GREEN + Style.BRIGHT + "You killed {}!".format(enemy.name) + Fore.WHITE + Back.BLACK + Style.NORMAL)
		else:
			print("{} HP is now {}.".format(enemy.name, enemy.hp))
			
	def heal(self):
		consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
		if not consumables:
			print("You don't have any items to heal you!")
			return
			
		for i, item in enumerate(consumables, 1):
			print("Choose an item to use to heal: ")
			print("{}. {}".format(i,item))
			
		valid = False
		while not valid:
			choice = input("")
			try:
				toEat = consumables[int(choice) - 1]
				self.hp = min(1000, self.hp + toEat.healingValue)
				self.inventory.remove(toEat)
				print("Current HP: {}".format(self.hp))
				valid = True
			except(ValueError,IndexError):
				print("Invalid choice, try again.")
			
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
	
	def moveNorth(self):
		self.move(dx=0, dy=-1)
	
	def moveSouth(self):
		self.move(dx=0, dy=1)
	
	def moveEast(self):
		self.move(dx=1, dy=0)
	
	def moveWest(self):
		self.move(dx=-1, dy=0)