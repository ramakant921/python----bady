import random

def play():
    print("🎮 Rock-Paper-Scissors Game 🎮")
    print("Type 'rock', 'paper', or 'scissors' (or 'quit' to stop)")

    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("\nYour choice: ").lower()
        if user == "quit":
            print("Thanks for playing! 👋")
            break
        if user not in choices:
            print("❌ Invalid choice! Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("😐 It's a tie!")
        elif (
            (user == "rock" and computer == "scissors")
            or (user == "paper" and computer == "rock")
            or (user == "scissors" and computer == "paper")
        ):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

if __name__ == "__main__":
    play()
