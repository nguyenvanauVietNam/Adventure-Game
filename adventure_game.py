import time
import random
from datetime import datetime
import os

LOG_FILE = "game_history.log"
score = 0  # Initialize the score
player_name = ""  # Initialize the player name


def log_message(message):
    """Log a message with a timestamp to the log file."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{current_time} - {message}\n")


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_top_display():
    """Display the player's name and score at the top of the console."""
    clear_console()
    print(f"Player: {player_name} | Score: {score}")
    print("-" * 40)


def print_pause(message, delay=1):
    """Print a message, wait for the delay, and then clear the screen."""
    show_top_display()
    print(message)
    time.sleep(delay)
    show_top_display()


def get_valid_input(prompt, options):
    """Get a valid input from the user based on the given options."""
    while True:
        show_top_display()
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print_pause("Invalid choice. Please try again.")


def intro():
    """Introduction to the game."""
    global player_name
    show_top_display()
    player_name = input("Enter your name: ")
    log_message(f"Player's name is {player_name}.")
    print_pause(f"Welcome, {player_name}!")
    print_pause("You find yourself in a dark forest.")
    print_pause("There are two paths ahead.")
    print_pause("One path leads to a creepy old house, "
                "and the other leads to a cave.")


def choose_path():
    """Allow the player to choose a path and determine the outcome."""
    path = get_valid_input("Which path will you choose? (house/cave): ",
                           ["house", "cave"])
    if path == "house":
        enter_house()
    else:
        enter_cave()


def enter_house():
    """Scenario where the player enters the house."""
    global score
    print_pause("You cautiously approach the house.")
    print_pause("As you enter, you hear strange noises coming from upstairs.")
    action = get_valid_input("Do you want to investigate the noise or leave "
                             "the house? (investigate/leave): ",
                             ["investigate", "leave"])
    if action == "investigate":
        score += 10
        fight_monster()
    else:
        score -= 5
        print_pause("You quickly leave the house and run back to the forest.")
        choose_path()


def enter_cave():
    """Scenario where the player enters the cave."""
    global score
    print_pause("You carefully step into the cave.")
    print_pause("It's dark and cold inside.")
    outcome = random.choice(["treasure", "trap"])
    if outcome == "treasure":
        score += 20
        print_pause("You find a treasure chest filled with gold and jewels!")
        print_pause("Congratulations! You win!")
    else:
        score -= 10
        print_pause("You trigger a trap, and the cave starts to collapse!")
        print_pause("You couldn't escape in time.")
        print_pause("Game over.")


def fight_monster():
    """Scenario where the player fights a monster."""
    global score
    print_pause("A monster appears from the darkness!")
    choice = get_valid_input("Do you fight or run away? (fight/run): ",
                             ["fight", "run"])
    if choice == "fight":
        if random.randint(1, 2) == 1:
            score += 15
            print_pause("You bravely fight the monster and win!")
            print_pause("Congratulations! You win!")
        else:
            score -= 10
            print_pause("The monster overpowers you. You lose.")
            print_pause("Game over.")
    else:
        score -= 5
        print_pause("You run back to the safety of the forest.")
        choose_path()


def play_again():
    """Prompt the player to restart or exit the game."""
    global score
    log_message(f"Player: {player_name}, Final Score: {score}")
    print_pause(f"{player_name}, your final score is: {score}")
    choice = get_valid_input("Would you like to play again? (yes/no): ",
                             ["yes", "no"])
    if choice == "yes":
        print_pause("Restarting the game...")
        main()
    else:
        print_pause("Thanks for playing! Goodbye.")


def main():
    """Main function to run the game."""
    global score
    score = 0
    open(LOG_FILE, "w").close()
    intro()
    choose_path()
    play_again()


if __name__ == "__main__":
    main()
