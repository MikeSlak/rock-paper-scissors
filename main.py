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


import random

computer_choice = random.randint(0, 2)

if computer_choice == 0:
  computer_hand = rock
elif computer_choice == 1:
  computer_hand = paper
elif computer_choice == 2:
  computer_hand = scissors

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))

if choice >= 3:
  print('Invalid Number!')
else:
  if choice == 0:
    player_hand = rock
  elif choice == 1:
    player_hand = paper
  elif choice == 2:
    player_hand = scissors

  print(player_hand)
  print("computer Chose:")
  print(computer_hand)



  if choice == computer_choice:
    print('Draw!')
  elif choice == 0 and computer_choice != 1:
    print('You Win!')
  elif choice == 1 and computer_choice != 2:
    print('You Win!')
  elif choice == 2 and computer_choice != 0:
    print('You Win!')
  else:
    print('You Lose!')