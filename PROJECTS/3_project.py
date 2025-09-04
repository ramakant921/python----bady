import random




# l = ["Rock","Paper","Scissor"]
# r = "Rock"
# p="Paper"
# s = "Scissor"

# user = [r,p,s]

l = ("rock","paper","scissor")

user = input("Enter your option: ").lower
computer = random.Random()

if(user == computer):
    print("YOU LOOSE!",user and computer)

else:
    print("YOU WON!",user and computer) 