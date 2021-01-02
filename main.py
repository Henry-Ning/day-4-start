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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

choices = [rock, paper, scissors]
random_number = random.randint(0,2)


if user_input==1:
  print(paper)
  print(f"Computer chose: {choices[random_number]}")
elif user_input==2:
  print(scissors)
  print(f"Computer chose: {choices[random_number]}")
elif user_input==0:
  print(rock)
  print(f"Computer chose: {choices[random_number]}")

if user_input >= 3 or user_input < 0: 
  print("You typed an invalid number, you lose!") 
elif random_number == user_input:
  print("draw")
elif random_number == user_input+1 or random_number == user_input -2:
  print("lose")
else:
  print("win")