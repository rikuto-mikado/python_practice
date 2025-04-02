import random

choices = ["rock", "paper", "scissors"]
print("Welcome to the game!!")
print("Type 'quit' to exit the game ")

wins = 0
losses = 0
draws = 0
while True:
    player = input("\nEnter your choice (rock / paper / scissors / quit): ").lower()

    if player == "quit":
        print("Thank you for playing!!")
        break

    if player not in choices:
        print("Invalid input. Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Wow it's draw!!")
        draws += 1
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        print("Win!!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Score → Wins: {wins} / Losses: {losses} / Draws: {draws}")

print("\nFinal Score:")
print(f"Wins: {wins} / Losses: {losses} / Draws: {draws}")
