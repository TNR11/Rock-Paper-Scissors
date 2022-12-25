import random

user_wins = 0
com_wins = 0
choices = ["rock", "paper", "scissors"]


def calc_winner(usr, comp):
    global user_wins
    global com_wins
    if usr == "rock" and comp == "scissors":
        print("You won!")
        user_wins += 1
    elif usr == "paper" and comp == "rock":
        print("You won!")
        user_wins += 1
    elif usr == "scissors" and comp == "paper":
        print("You won!")
        user_wins += 1
    elif usr == comp:
        print("It's a draw!")
        user_wins += 1
        com_wins += 1
    else:
        print("You Lost! =(")
        com_wins += 1


while True:
    user_input = input("\nChoose: Rock, Paper or Scissors or Q to quit\n").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        print("invalid choice, choose again")
        continue
    com_input = random.randint(0, 2)
    com_choice = choices[com_input]
    print(f"Computer chose {com_choice}")
    calc_winner(user_input, com_choice)

print(f"\nUser wins: {user_wins} Computer wins: {com_wins} \n")
print("Goodbye!")
