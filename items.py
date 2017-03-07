from colorama import init, Fore, Back, Style
init()

class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects.")

	def __str__(self):
		return self.name

class RustyKnife(Weapon):
	def __init__(self):
		self.name = "Rusty Knife"
		self.description = "A small rusty knife. " \
		                   "it doesn't seem very durable."
		self.damage = 5
		
class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.description = "A reasonably sized dagger. " \
		                   "More dangerous than a rusty knife."
		self.damage = 10	
		
class Consumable:
	def __init__(self):
		raise NotImplementedError("Do not create raw Consumable objects.")
		
	def __str__(self):
		return "{} (+{} HP)".format(self.name, self.healingValue)

class MoldyBread(Consumable):
	def __init__(self):
		self.name = "Moldy Bread"
		self.healingValue = 50
		
class HealingPotion(Consumable):
	def __init__(self):
		self.name = "Potion of Healing"
		self.healingValue = 1000