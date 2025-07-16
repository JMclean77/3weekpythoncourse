import random

rock= "r"
paper= "p"
scissors= "s"

print("Welcome to Rock, Paper, Scissors!")
print()

p1_choice= input("Player 1 please choose \"r\", \"p\", \"s\":")
if p1_choice not in ["r", "p", "s"]:
    print("Player 1 choice must be \"r\", \"p\", \"s\":")
    quit()
elif p1_choice in ["r", "p", "s"]:
    print(f"Player 1 chose \"{p1_choice}\"")

p2_choice= ["r", "p", "s"]
p2_choice= random.choice(p2_choice)
print(f"Player 2 chose: \"{p2_choice}\"")

if p1_choice == p2_choice:
    print("It's a Tie!")
elif p1_choice == scissors and p2_choice == paper:
    print("Player 1 Wins!")
elif p1_choice == rock and p2_choice == scissors:
    print("Player 1 Wins!")
elif p1_choice == paper and p2_choice == rock:
    print("Plater 1 Wins!")
elif p1_choice == paper and p2_choice == scissors:
    print("Player 2 Wins!")
elif p1_choice == scissors and p2_choice == rock:
    print("Player 2 Wins!")
elif p1_choice == rock and p2_choice == paper:
    print("Plater 2 Wins!")

