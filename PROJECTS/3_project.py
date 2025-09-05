import random

def play():
    print("Rock,Paper,Scissor  GAME!")
    print("Type (rock,paper,scissor) or (quit/stop)")
    
    choices = ("rock","paper","scissor")

    while True:
        user = input("Enter your option: ").lower()
        if(user == "quit"):
            print("Thanks For playing")
            break
        if (user not in choices):
            print("Invalid Choice! Try Again") 
            continue
        
        
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        if (user == computer):
            print("It's a tie!")
            
        elif ((user == "rock" and computer == "scissor") or
              (user == "scissor" and computer == "paper") or
              (user =="paper" and computer == "rock")):
            print("YOU WON!")
            
        else:
            print("YOU LOOSE! COMPUTER WINS.") 
                
if __name__ == "__main__":               
    play()