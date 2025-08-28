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
    if((computer - user ) == -1 or (computer - user ) == 2):
        print("You lose")
    else:
        print("You won!")