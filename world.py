import enemies
import random
from colorama import init, Fore, Back, Style
init()

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def introText(self):
		raise NotImplementedError("Crate a subclass instead!")
		
	def modifyPlayer(self, player):
		pass
		

class StartTile(MapTile):
	def introText(self):
		return """
		You find yourself in Count Nefarious's dungeons located inside the dreaded Castle Evil!
		You see light emanating from a doorway to the north.
		"""

class MidTile(MapTile):
	def introText(self):
		return """
		This is a rather boring hallway, though the light to the north is getting brighter.
		"""

class NormalTile(MapTile):
	def introText(self):
		return """
		An empty room
		"""
		
class EnemyTile(MapTile):
	def __init__(self,x,y):
		r=random.random()
		if r < 0.50:
			self.Enemy = enemies.Skeleton()
			self.aliveText = "Bones on the ground form into a skeleton!"
			self.deadText = "There is nothing left in the room but a pile of bones"
		elif r < 0.80:
			self.Enemy = enemies.BatColony()
			self.aliveText = "You gear a squeaking noise growing louder" \
			                 "...Suddenly you are lost in a swarm of bats!"
			self.deadText = "The corpses of dead bats litter the ground"
		elif r < 0.95:
			self.Enemy = enemies.Wizard()
			self.aliveText = "A wizard suddenly teleports in!"
			self.deadText = "The body of the evil wizard lays still on the floor"
		else:
			self.Enemy = enemies.CountNefarious()
			self.aliveText = "It's the evil Count Nefarious! God help you, Adventurer."
			self.deadText = "how"
		
		super().__init__(x,y)
	
	def introText(self):
		text = self.aliveText if self.Enemy.isAlive() else self.deadText
		return text
			
	def modifyPlayer(self, player):
		if self.Enemy.isAlive():
			player.hp = player.hp - self.Enemy.damage
			print("Enemy does {} damage. You have {} HP remaining.".format(self.Enemy.damage, player.hp))

class VictoryTile(MapTile):
	def introText(self):
		return """
		The light you saw is getting brighter still...
		... It grows as you get closer! It's sunlight!
		
		Turns out the dreaded Castle Evil was only a few hallways long. Who woulda thought?
		Victory is yours!
		"""
		
world_map = [
	[NormalTile(0,0),VictoryTile(1,0),EnemyTile(2,0)],
	[EnemyTile(0,1),MidTile(1,1),NormalTile(2,1)],
	[NormalTile(0,2),StartTile(1,2),EnemyTile(2,2)]
]

def tileAt(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None