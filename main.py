import pygame
import time
import random

from battle import BattleMode
from enemy import RightPathEnemies

pygame.mixer.init()

CheckpointOne = False
CheckpointTwo = False 
CheckpointThree = False

UserInputedName = ""

ItemDict = {"Potions": 0, "Arrows": 0, "Points": 0, "Shards": 0, "Wand": 0} # Player item storage
StatDict = {"Max Magic": 100, "Current Magic": 100, "Max Health": 15, "Current Health": 15, "Level": 1} # Player stats storage


MovesDict = {"StoneFist": 5, "Harden": 5}
BattleMenu = f"| 1. Inventory | 2. Attack | 3. Give Up | {StatDict} |" # Menu when battling
StartingPathwayDict = {"right": "you noted the thin entrance, covered in mold.", "left": "you felt a burning sensation; it was nothing that you've experienced before.", "center":" you felt at ease, as if you weren't here at all." } # Pathway diolo






# Starting inputs
while CheckpointOne == False:
	Menu = input("(1. Start  2. Load): ")
	if Menu not in ["1", "2"]:
		print("try again")
	elif Menu == "1":
		time.sleep(1)
		UserInputedName = input("What is your name?: ")
		time.sleep(1)
		input("Press Enter to continue...")
		CheckpointOne = True
	elif Menu == "2":
		print("coming soon")



# Second gameplay section
while CheckpointTwo == False:
	print("You wake up in a pond; you've been here before.")
	time.sleep(2)
	print(f"You recognize your face. Your name is {UserInputedName}.")
	input("... ")
	print("You see three different pathways in front of you.")
	time.sleep(2)
	print("The pathways are on the left, right, and center.")
	time.sleep(2)
	StartingPathway = input("Which one do you walk down? (right, left, center): ")
	if StartingPathway not in ["Right", "right", "Left", "left", "Center", "center"]:
		AutoStarterPath = ['right', "left", "center"]
		StartingPathway = random.choice(AutoStarterPath)
		print(f"As you entered the path to the {StartingPathway}, {StartingPathwayDict[StartingPathway]} (Auto Pick)")
		input("... ")
		CheckpointTwo = True
	else:
		StartingPathway = StartingPathway.lower()
		print(f"As you entered the path to the {StartingPathway}, {StartingPathwayDict[StartingPathway]}")
		input("... ")
		CheckpointTwo = True

	# Third gameplay section (right pathway)
	while CheckpointThree == False:
		if StartingPathway == "right":
			EnemyChoice = random.choice(RightPathEnemies)
			print(f"You see a {EnemyChoice.name} up ahead in the pathway.")
			time.sleep(2)
			print("It reeks of dead insects and is covered in some sort of black moss.")
			time.sleep(2)
			FirstFight = input("(1. Go around it  2. Fight it)")
			if FirstFight not in ["1", "2"]:
				FirstFight = random.choice(["1", "2"])
				print('Auto Choice')
			if FirstFight == "1":
				print(f"You try to go around the {EnemyChoice.name} unnoticed.")
				time.sleep(2)
				print("It ends up seeing you.")
				time.sleep(2)
				print("As its rocky body swings at you, you pick up a stick to defend yourself.")
				time.sleep(2)
				print("You realize that the stick is actually a magic wand; it's time to fight.")
				time.sleep(2)
			else:
				print("You reach for your magic stick to attack the monster")


			
			EnemyHealth = EnemyChoice.health
					
			BattleMode(f"{EnemyChoice.name}", f"{EnemyHealth}", StatDict, ItemDict)
			CheckpointThree = True






















'''
pygame.mixer.music.load("hellohibye.mp3")
pygame.mixer.music.play()

BattleMode(f"{EnemyChoice}", f"{EnemyHealth}")
'''
		#Third gameplay section (left pathway)
'''
		if StartingPathway == "left":
			print("You see a giant bumblebee up ahead in the pathway.")
			time.sleep(2)
			print("It smells of honey and grass")
			time.sleep(2)
			FirstFight = input("(1. Go around it  2. Fight it)")
			if FirstFight not in ["1", "2"]:
				FirstFight = random.choice(["1", "2"])
				print('Auto Choice')
			if FirstFight == "1":
				print("You try to go around the bumblebee unnoticed.")
				time.sleep(2)
				print("It ends up seeing you.")
				time.sleep(2)
				print("As its flakey body swings at you, you pick up a stick to defend yourself.")
				time.sleep(2)
				print("You realize that the stick is actually a magic wand; it's time to fight.")
				time.sleep(2)
				BeeHealth = 20
				InBattle = True
			else:
				print("You reach for your magic stick to attack the monster")
				time.sleep(2)
				BeeHealth = 20
				InBattle = True

			print("--- BATTLE STARTED ---")
			while InBattle:
				BattleMenu = f"| 1. Inventory | 2. Attack | 3. Give Up | {StatDict} |"
				print(BattleMenu)
				BattleChoice = input("Choose an action: ")

				if BattleChoice == "1":
					print(ItemDict)

				elif BattleChoice == "2":
					PlayerDamage = random.randint(4, 8)
					BeeHealth -= PlayerDamage
					print(f"You strike the bumblebee for {PlayerDamage}!")
					time.sleep(1)

					if BeeHealth <= 0:
						print("The bumblebee dies")
						ItemDict['Points'] += 10
						print("Victory! You gained 10 points.")
						InBattle = False
						CheckpointThree = True
						break

					BeeAttack = random.randint(3, 5)
					StatDict["Current Health"] -= BeeAttack
					print(f"The giant bee strikes you back for {BeeAttack} damage!")
					time.sleep(1)

					if StatDict["Current Health"] <= 0:
						print("You die")
						exit()

				elif BattleChoice == "3":
					print("Game Over")
					exit()


		#Third gameplay section (center pathway)
		if StartingPathway == "center":
			print("You see a giant tiger up ahead in the pathway.")
			time.sleep(2)
			print("It looks holy.")
			time.sleep(2)
			FirstFight = input("(1. Go around it  2. Fight it)")
			if FirstFight not in ["1", "2"]:
				FirstFight = random.choice(["1", "2"])
				print('Auto Choice')
			if FirstFight == "1":
				print("You try to go around the golem unnoticed.")
				time.sleep(2)
				print("It ends up seeing you.")
				time.sleep(2)
				print("As its rocky body swings at you, you pick up a stick to defend yourself.")
				time.sleep(2)
				print("You realize that the stick is actually a magic wand; it's time to fight.")
				time.sleep(2)
				GolemHealth = 20
				InBattle = True
			else:
				print("You reach for your magic stick to attack the monster")
				time.sleep(2)
				GolemHealth = 20
				InBattle = True

			print("--- BATTLE STARTED ---")
			while InBattle:
				BattleMenu = f"| 1. Inventory | 2. Attack | 3. Give Up | {StatDict} |"
				print(BattleMenu)
				BattleChoice = input("Choose an action: ")

				if BattleChoice == "1":
					print(ItemDict)

				elif BattleChoice == "2":
					PlayerDamage = random.randint(4, 8)
					GolemHealth -= PlayerDamage
					print(f"You strike the golem for {PlayerDamage}!")
					time.sleep(1)

					if GolemHealth <= 0:
						print("The golem dies")
						ItemDict['Points'] += 10
						print("Victory! You gained 10 points.")
						InBattle = False
						CheckpointThree = True
						break

					GolemAttack = random.randint(3, 5)
					StatDict["Current Health"] -= GolemAttack
					print(f"The golem strikes you back for {GolemAttack} damage!")
					time.sleep(1)

					if StatDict["Current Health"] <= 0:
						print("You die")
						exit()

				elif BattleChoice == "3":
					print("Game Over")
					exit()
					'''