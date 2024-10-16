# # You can use this workspace to write and submit your adventure game project.
# #print Print descriptions of what's happening for the player
# print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
# print("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village...")

# #Pausing between printing descriptions
# import time
# print("Hello")
# time.sleep(2)
# print("world!")

# #Give the player some choices
# print("Enter 1 to knock on the door of the house.")
# print("Enter 2 to peer into the cave.")
# choice = input("What would you like to do? (Please enter 1 or 2): ")

# if choice == '1':
#     print("You walk up to the door of the house and knock. A voice calls out asking who you are.")
# elif choice == '2':
#     print("You peer cautiously into the cave. It's dark and spooky, but you feel a sense of adventure.")
# else:
#     print("Invalid choice. Please enter 1 or 2.")

# #Make sure the player gives a valid input
# def valid_input(prompt):
#     while True:
#         choice = input(prompt)
#         if choice in ['1', '2']:
#             return choice
#         else:
#             print("Please enter 1 or 2.")

# print("valid_input: ", valid_input("Enter 1 or 2: "))

# #Add functions and refactor your code
# def fight():
#     print("You engage in a fierce battle!")
#     # Add more details about the fight, outcomes, and choices here
#     # For example, you could ask the player if they want to attack or flee

# def cave():
#     print("You enter the dark cave. It's damp and eerie.")
#     # Describe what the player sees and what choices they have
#     # For example, you could give options to explore deeper or leave the cave

# def field():
#     print("You run back to the field. The sun is shining brightly.")
#     # Describe the field and what the player can do next
#     # For example, you could offer choices to go back to the house or explore the forest

# def house():
#     print("You approach the house. The door is slightly ajar.")
#     # Describe the house and what the player can do inside
#     # For example, you could ask if they want to knock on the door or enter

# # Example of how to call these functions based on player choice
# def main():
#     print("Welcome to the Adventure Game!")
#     choice = valid_input("Enter 1 to fight.\nEnter 2 to explore the cave.\n(Please enter 1 or 2): ")
    
#     if choice == '1':
#         fight()
#     elif choice == '2':
#         cave()
#     elif choice == '3':
#         field()
#     elif choice == '4':
#         house()
#     else:
#         print("Invalid choice. Please enter 1 or 2 or 3 or 4.")   

# # Start the game
# main()


#this my game suggestions
import time
import random
from datetime import datetime
import os

LOG_FILE = "game_history.log"
score = 0  # Initialize the score
player_name = ""  # Initialize the player name

def log_message(message):
    """Log a message with a timestamp to the log file."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current system time
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{current_time} - {message}\n")

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_top_display():
    """Display the player's name and score at the top of the console."""
    clear_console()
    print(f"Player: {player_name} | Score: {score}")
    print("-" * 40)  # Separator line

def print_pause(message, delay=1):
    """Print a message, wait for the delay, and then clear the screen."""
    show_top_display()  # Show the top display first
    print(message)  # Print the current message
    time.sleep(delay)
    show_top_display()  # Clear the screen while keeping the top display

def get_valid_input(prompt, options):
    """Get a valid input from the user based on the given options."""
    while True:
        show_top_display()  # Update display
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print_pause("Invalid choice. Please try again.")

def intro():
    """Introduction to the game."""
    global player_name
    # Get the player's name at the start
    show_top_display()
    player_name = input("Enter your name: ")
    log_message(f"Player's name is {player_name}.")
    print_pause(f"Welcome, {player_name}!")
    print_pause("You find yourself in a dark forest.")
    print_pause("There are two paths ahead.")
    print_pause("One path leads to a creepy old house, and the other leads to a cave.")

def choose_path():
    """Allow the player to choose a path and determine the outcome."""
    path = get_valid_input("Which path will you choose? (house/cave): ", ["house", "cave"])
    if path == "house":
        enter_house()
    else:
        enter_cave()

def enter_house():
    """Scenario where the player enters the house."""
    global score
    print_pause("You cautiously approach the house.")
    print_pause("As you enter, you hear strange noises coming from upstairs.")
    action = get_valid_input("Do you want to investigate the noise or leave the house? (investigate/leave): ", ["investigate", "leave"])
    if action == "investigate":
        score += 10  # Increase score for bravery
        fight_monster()
    else:
        score -= 5  # Decrease score for leaving
        print_pause("You quickly leave the house and run back to the forest.")
        choose_path()

def enter_cave():
    """Scenario where the player enters the cave."""
    global score
    print_pause("You carefully step into the cave.")
    print_pause("It's dark and cold inside.")
    outcome = random.choice(["treasure", "trap"])
    if outcome == "treasure":
        score += 20  # Increase score for finding treasure
        print_pause("You find a treasure chest filled with gold and jewels!")
        print_pause("Congratulations! You win!")
    else:
        score -= 10  # Decrease score for falling into a trap
        print_pause("You trigger a trap, and the cave starts to collapse!")
        print_pause("You couldn't escape in time.")
        print_pause("Game over.")

def fight_monster():
    """Scenario where the player fights a monster."""
    global score
    print_pause("A monster appears from the darkness!")
    choice = get_valid_input("Do you fight or run away? (fight/run): ", ["fight", "run"])
    if choice == "fight":
        if random.randint(1, 2) == 1:
            score += 15  # Increase score for defeating the monster
            print_pause("You bravely fight the monster and win!")
            print_pause("Congratulations! You win!")
        else:
            score -= 10  # Decrease score for losing to the monster
            print_pause("The monster overpowers you. You lose.")
            print_pause("Game over.")
    else:
        score -= 5  # Decrease score for running away
        print_pause("You run back to the safety of the forest.")
        choose_path()

def play_again():
    """Prompt the player to restart or exit the game."""
    global score
    log_message(f"Player: {player_name}, Final Score: {score}")  # Log player name and final score
    print_pause(f"{player_name}, your final score is: {score}")
    choice = get_valid_input("Would you like to play again? (yes/no): ", ["yes", "no"])
    if choice == "yes":
        print_pause("Restarting the game...")
        main()
    else:
        print_pause("Thanks for playing! Goodbye.")

def main():
    """Main function to run the game."""
    global score
    score = 0  # Reset score at the start of a new game
    # Clear the log file at the start of a new game session
    open(LOG_FILE, "w").close()
    intro()
    choose_path()
    play_again()

# Run the game
if __name__ == "__main__":
    main()

