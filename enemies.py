from colorama import init, Fore, Back, Style
init()

class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")
		
	def __str__(self):
		return self.name
	
	def isAlive(self):
		return self.hp > 0
		
class Skeleton(Enemy):
	def __init__(self):
		self.name = "Skeleton"
		self.hp = 10
		self.damage = 2
		
class CountNefarious(Enemy):
	def __init__(self):
		self.name = "Count Nefarious"
		self.hp = 200
		self.damage = 50

class BatColony(Enemy):
	def __init__(self):
		self.name = "Colony of bats"
		self.hp = 100
		self.damage = 4

class Wizard(Enemy):
	def __init__(self):
		self.name = "Wizard"
		self.hp = 20
		self.damage = 20