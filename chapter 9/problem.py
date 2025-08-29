# Problem 1

# f = open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("The word twinkle is present in the content")

# else:
#     print("The word twinkle is not present in the content")
    
# f.close()   



# Problem 2

# import random

# def game():
#     print("You are playing the game...")
#     score = random.randint(1,62)
#     # Fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0   
            
             
#     print(f"Your score: {score}")
#     if(score > hiscore):
#         # write this hiscore file
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
            
            
#     return score

# game()



# Problem 3

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
        
#     with open(f"table/table_{n}.txt","w") as f:
#         f.write(table)
        
        


# for i in range(2,21):
#     generateTable(i)



# Problem 4

# word = "donkey"

# with open("file.txt","r") as f:
#     content = f.read()
    
# contentNew = content.replace("donkey","######")

# with open("file.txt","w") as f:
#     f.write(contentNew)



# Problem 5

# words = ["Donkey","good","ganda"]

# with open("file.txt","r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word,"#" * len(word))

# with open("file.txt","w") as f:
#     f.write(content)



# Problem 6

# with open("log.txt") as f:
#     content = f.read()
    
# if("python" in content):
#     print("Yes python is present")
    
# else:
#     print("No it is not present")



# Problem 7

# with open("log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:    
#     if("python" in line):
#         print(f"Yes python is present. Line no: {lineno}")
#         break
#     lineno += 1
    
# else:
#     print("No it is not present")



# Problem 8

with open("this.txt")