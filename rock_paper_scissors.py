import random

player_score = 0
computer_score = 0

player_choice = ""
computer_choice = ""
NUM_ROUNDS = 5

def computerPlay():
    number = random.randint(1, 3)
    if number == 1:
        return "Rock"
    elif number == 2: 
        return "Paper"
    else: 
        return "Scissors"

def play_round(playerSelection, computerSelection):
    playerSelection = input("Rock, Paper, Scissors: ")
    computerSelection = computerPlay()
    check_answer(playerSelection, computerSelection)

def check_answer(playerSelection, computerSelection):
    while (playerSelection.casefold() == computerSelection.casefold()):
        print(f"\nBoth contestants used {playerSelection}. Try again\n")
        playerSelection = input("Rock, Paper, Scissors: ")
        computerSelection = computerPlay()
    check_final_answer(playerSelection, computerSelection)
    display_choices(playerSelection, computerSelection)

def check_final_answer(playerSelection, computerSelection):
    global player_score, computer_score
    if playerSelection.casefold() == "rock":
        if computerSelection.casefold() == "paper":
            computer_score += 1
            return "You lose! Paper beats rock"
        else:
            player_score += 1
            return "You win! Rock beats scissors"
    elif playerSelection.casefold() == "paper":
        if computerSelection.casefold() == "rock":
            player_score += 1
            return "You win! Paper beats rock"
        else:
            computer_score += 1
            return "You lose! Scissors beats paper"
    elif playerSelection.casefold() == "scissors":
        if computerSelection.casefold() == "rock":
            computer_score += 1
            return "You lose! Rock beats scissors"
        else:
            player_score += 1
            return "You win! Scissors beat paper"

def display_choices(playerSelection, computerSelection):
    print(f"\nThe player chose {playerSelection}")
    print(f"The computer chose {computerSelection}\n")

def score_tracker():
    print(f"Player's score is {player_score} and computer's score is {computer_score}")
    if player_score == (NUM_ROUNDS-2):
        print(f"Player won {player_score} points out of 5. Player wins!")
    elif computer_score == (NUM_ROUNDS-2):
        print(f"Computer won {computer_score} points out of 5. Computer wins!")

def game():
    while player_score < (NUM_ROUNDS-2) and computer_score < (NUM_ROUNDS-2):
        play_round(player_choice, computer_choice)
        score_tracker()



print("\nWelcome to Rock Paper Scissors")
game()