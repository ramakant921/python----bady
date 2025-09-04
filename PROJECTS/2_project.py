# THIS IS A SIMPLE NUMBER GUESSING GAME FOR BASICS


import random

while True:
    
    user = int(input("Enter the number between 1-10: "))
    computer = random.randint(1,11)


    if user == computer:
        print("YOU WON!👌",user and computer)

    else:
        print("YOU LOOSE!✌️",user and computer)
        
        play_again = input("Do you want to play again? (y/n)").lower()
        if(play_again != "y"):
            print("THANKS FOR PLAYING, NIGGA")
            break