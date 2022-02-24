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
user_choice = input("what do u want to choose? type 0 for rock, 1 for paper or 2 for scissors.\n")

computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")
if user_choice == 0 and computer_choice ==2:
    print('y')
elif user_choice > computer_choice:
print("you lose!")