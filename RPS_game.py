#Rock Paper Seasor Game 

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("what do you want to select? 0 for Rock, 1 for Paper , 2 for seasors.\n"))
print(game_images[user_choice])

AI_choice  = random.randint(0,2)
print("AI choice:")
print(game_images[AI_choice])

if user_choice >= 3 or user_choice <  0:
    print("INVALID_CHOICE")
elif user_choice ==0 and AI_choice == 2:
    print("You Win!")
elif AI_choice == 0 and user_choice == 2:
  print("You lose")
elif AI_choice > user_choice:
  print("You lose")
elif user_choice > AI_choice:
  print("You win!")
elif AI_choice == user_choice:
  print("It's a draw")

