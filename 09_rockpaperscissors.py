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

#Write your code below this line 👇


z = (input("What do you want to chose: Type R for rock, P for paper and S for scissors."))
a = z.upper()
if a == 'R':
    print("You chose:")
    print(f"{rock}")
elif a == 'P':
    print("You chose:")
    print(f"{paper}")
elif a == 'S':
    print("You chose:")
    print(f"{scissors}")
else:
    print("INVALID INPUT!!!")
    
choice = [rock, paper ,scissors]
print("Computer chose: ")
b = random.randint(0, 2)
print(choice[b])

if a == 'R' and b == 0:
    print("Both are same, It's a draw!")
elif a == 'R' and b == 1:
    print("You lose!!")
elif a == 'R' and b == 2:
    print("You won!!")
elif a == 'P' and b == 0:
    print("You won!!")
elif a == 'P' and b == 1:
    print("Both are same, It's a draw!")
elif a == 'P' and b == 2:
    print("You lose!!")
elif a == 'S' and b == 0:
    print("You lose!!")
elif a == 'S' and b == 1:
    print("You won!!")
elif a == 'S' and b == 2:
    print("Both are same, It's a draw!")





