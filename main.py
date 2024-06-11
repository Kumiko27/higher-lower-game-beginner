from os import system, name
from art import logo
from art import vs
from game_data import data
import random

# Declare global variable
player_score = 0
game_over = False


# Clear the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


# Function to pick a celebrity from list
def get_celebrity():
    """Choose a random celebrity from the list"""
    return random.choice(data)


# Function to format the celebrity output
def format_print(celebrity):
    """Format the output of the celebrity sent"""
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}."


def compare(celebrity_A, celebrity_B):
    """Returns which celebrity has more follower A or B"""
    if celebrity_A > celebrity_B:
        return "A"
    else:
        return "B"


# Get celebrity to compare
compare_A = get_celebrity()
compare_B = get_celebrity()

while not game_over:
    # Print logo
    clear()
    print(logo)

    # Display score if there is already one
    if player_score > 0:
        print(f"You're right! Current score: {player_score}")

    # Print first celebrity to compare
    print("Compare A: " + format_print(compare_A))
    print(vs)

    # Print second celebrity to compare
    print("Against B: " + format_print(compare_B))

    # Ask the user to guess
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    # Call function to determine who wins
    correct_choice = compare(compare_A['follower_count'], compare_B['follower_count'])
    # check if user is correct
    if user_choice == correct_choice:
        # increase user score and change the comparison
        player_score += 1
        compare_A = compare_B
        compare_B = get_celebrity()
    else:
        # the game is over
        game_over = True
        print(f"Sorry, that's wrong. Final score: {player_score}")
