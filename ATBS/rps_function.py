import random


def get_player_choice():
    """Ask until the player enters r, p, s or q. Return the choice."""
    while True:
        choice = input("Enter your choice: (r)ock, (p)aper, (s)cissors or (q)uit: ").lower().strip()
        if choice in ["r", "p", "s", "q"]:
            return choice
        print("Invalid choice. Please try again.")


def decide_winner(player, computer):
    """Return 'win', 'lose' or 'tie' from the player's point of view."""
    if player == computer:
        return "tie"
    if (player == "r" and computer == "s") or \
       (player == "p" and computer == "r") or \
       (player == "s" and computer == "p"):
        return "win"
    return "lose"


def play():
    wins = losses = ties = 0
    while True:
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")
        print("Rock, Paper, Scissors, Shoot!")

        player = get_player_choice()
        if player == "q":
            print("Thanks for playing!")
            return

        computer = random.choice(["r", "p", "s"])
        print(f"{player} vs. {computer}")

        result = decide_winner(player, computer)
        if result == "win":
            print("You win!")
            wins += 1
        elif result == "lose":
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1


#play()