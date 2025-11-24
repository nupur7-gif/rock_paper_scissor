import random

def input_from_user():
    options = ["rock", "paper", "scissors"]
    name = input("Enter the name of user: ")
    user_input = input("Enter a choice for the game to begin, %s: " % name).lower()
    while user_input not in options:
        print("Invalid input, %s! Try again." % name)
        user_input = input("Enter a choice for the game to begin, %s: " % name).lower()
    return user_input, name

def computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def rules():
    print("User gives an input from the options and computer gives an input randomly")
    print('''The winner is determined by the following rules:
             Rock beats Scissors (Rock crushes Scissors).
             Scissors beat Paper (Scissors cut Paper).
             Paper beats Rock (Paper covers Rock).
             If both user and computer choose the same shape, the game is a tie and is typically replayed until someone wins.''')

def the_game(user, computer, user_score, computer_score):
    if (user == computer):
        print("It's a tie! Try again.")
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        print("WOHOO! You win!!")
        user_score += 1
    else:
        print("Oh no! You lose. Try again.")
        computer_score += 1
    return user_score, computer_score

def display_score(user_score, computer_score):
    print("Scoreboard:")
    print("User: %d || Computer: %d" % (user_score, computer_score))

def main_menu():
    user_score = 0
    computer_score = 0
    print("WELCOME TO THE GAME!!")
    print("Let's rock, paper and scissors!!")
    print("*" * 10)
    print("Menu")
    print("*" * 10)
    while True:
        choice = int(input("Press 1 for play \nPress 2 for rules \nPress 3 for scoreboard \nPress 4 for exit: "))
        if (choice == 1):
            user, name = input_from_user()
            computer = computer_choice()
            print("%s chose: %s" % (name, user))
            print("Computer chose: %s" % computer)
            user_score, computer_score = the_game(user, computer, user_score, computer_score)
            display_score(user_score, computer_score)
        elif (choice == 2):
            rules()
        elif (choice == 3):
            display_score(user_score, computer_score)
        elif (choice == 4):
            print("Thanks forplaying!!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")

main_menu()