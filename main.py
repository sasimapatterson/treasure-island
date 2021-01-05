print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You are lost in the jungle and trying to find your way out. Which way do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
  choice2 = input('You reach to the flood zone. Type "wait" if you want to wait for the water level to go down which might take days or "swim" to get to the other side faster but may take risk. \n').lower()
  if choice2 == "wait":
    choice3 = input('You mange to cross the flood zone safely. The treasure is in the house infront of you. Which door would you choose? Type "blue", "red" or "yellow" \n').lower()
    if choice3 == "yellow":
      print("Congratulation, you win!")
    elif choice3 == "red":
      print("Game Over. Burned by fire.")
    elif choice3 == "blue":
      print("Game Over. You walked into a poopy trap")
    else:
      print("Game Over!")
  else:
    print("Game Over! You got sucked into a whale'\s gut") 
else:
  print("Game Over! A big rock just fell right on you")

