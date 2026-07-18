
import pygame
import time
import random
def BattleMode(EnemyName, EnemyHealth, StatDict, ItemDict):
	print("======================")
	print("--- BATTLE STARTED ---")
	print("======================")
	InBattle = True 
	EnemyHealth = int(EnemyHealth)
	while InBattle == True:
		BattleMenu = f"| 1. Inventory | 2. Attack | 3. Special Attack | 4. Give Up | {StatDict} |"
		print(BattleMenu)
		BattleChoice = input("Choose an action: ")

		if BattleChoice == "1":
			print(ItemDict)

		elif BattleChoice == "2":
			PlayerDamage = random.randint(4, 8)
			EnemyHealth -= PlayerDamage
			print(f"You strike the {EnemyName} for {PlayerDamage}!")
			time.sleep(1)

			if EnemyHealth <= 0:
				print(f"The {EnemyName} dies")
				ItemDict['Points'] += 10
				print("Victory! You gained 10 points.")
				InBattle = False
				break

			EnemyAttack = random.randint(3, 5)
			StatDict["Current Health"] -= EnemyAttack
			print(f"The {EnemyName} strikes you back for {EnemyAttack} damage!")
			time.sleep(1)

			if StatDict["Current Health"] <= 0:
				print("You die")
				exit()

		elif BattleChoice == "3":
			print("Game Over")
			exit()