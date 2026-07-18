class Enemy:
	def __init__(self, name, health, defence, AttackOne, AttackTwo):
		self.name = name
		self.health = health
		self.defence = defence
		self.AttackOne = AttackOne
		self.AttackTwo = AttackTwo

RightPathEnemies = [
					Enemy("Golem", 15, 0, "a", "b"), 
					Enemy("Stone_Talus", 15, 0, "c", "d"), 
					Enemy("Elderwood", 15, 0, "e", "f"), 
					Enemy("Rot_Priest", 15, 0, "g", "h")]