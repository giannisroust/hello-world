import random

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print("Rock, Paper, Scissors, Shoot!")
    while True:
        pl_choice = input("Enter your choice (r)ock, (p)aper, (s)cissors) or (q)uit: ").lower()
        if pl_choice == "q":
            raise SystemExit
        if pl_choice in ["r", "p", "s"]:
            break
        print("Invalid choice. Please try again.")

    comp_choice = random.choice(["r", "p", "s"])
    print(pl_choice + " vs. " + comp_choice)
    if pl_choice == comp_choice:
        print("It's a tie!")
        ties += 1
    elif (pl_choice == "r" and comp_choice == "s") or \
         (pl_choice == "p" and comp_choice == "r") or \
         (pl_choice == "s" and comp_choice == "p"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
