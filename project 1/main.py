import random


computer = random.choice([1,0,-1])
userstr = input("Enter your choice: ")
userDict = {"s":1,  "w":-1,  "g":0}
reverseDict = {1:"Snake",  -1:"Water   ",  0:"Gun"}

user = userDict[userstr]


print(f"You choose: {reverseDict[user]} \nComputer choice: {reverseDict[computer]}")

if( computer == user):
    print("It's draw!")
    
    
else:    
    if(computer == -1 and user == 1):
        print("You win!")
        
    elif(computer == -1 and user == 0):
        print("You loose!")
        
    elif(computer == 1 and user == 0):
        print("You win!")
        
    elif(computer == 1 and user == -1):
        print("You loose!")
        
    elif(computer == 0 and user == -1):
        print("You win!")
        
    elif(computer == 0 and user == -1):
        print("You win!")
        
    else:
        print("Something went wrong❎")
        
        
if((computer - user ) == -1 or (computer - user ) == 2):
    print("You lose")
    
else:
    print("You won!")