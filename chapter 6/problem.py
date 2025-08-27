# Problem 1

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1: ",a1)
    
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2: ",a2)
    
# elif(a3>a2 and a3>a1 and a3>a4):
#     print("Greatest number is a3: ",a3)
    
# elif(a4>a2 and a4>a3 and a4>a1):
#     print("Greatest number is a4: ",a4)
    
    

    # Problem 2
    
# mark1 = int(input("enter marks 1: "))    
# mark2 = int(input("enter marks 2: "))    
# mark3 = int(input("enter marks 3: "))    
 
# # check for total percentage
# total_percentage = ((mark1+mark2+mark3)/300)*100

# if(total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
#     print("You have passed exam: ",total_percentage)
    
# else:
#     print("You have failed exam: ",total_percentage)
    
    
    
    # Problem 3
    
# c1= "make a lots of money"
# c2= "buy now"
# c3= "subscribe now"
# c4= "click this"   
# c5= "and all set"
        
# comments = input("Enter comments: ")

# if((c1 in comments) or (c2 in comments) or (c3 in comments) or (c4 in comments)):
    
#     print("It's a spam comment")
    
# elif(c5 in comments):
#     print("It's the best word!") 
    
# else:
#     print("It's a true comment")



# Problem 4

# name = input("Enter name: ")

# if(len(name)<10):
#     print("Your username contain less than 10 character")
    
# elif(len(name)>10):
#     print("Your username contain greater than 10 character")




#  Problem 5

# name = ["Harrison","Vidya","Romit","Shashwat","Ubon"]

# l = input("Enter name: ")

# if(l in name):
#     print("Entered name is presented in the list")
    
# else:
#     print("Entered name is not presented in list")    



# Problem 6

# marks = int(input("Enter your Marks: "))

# if(90<= marks<=100):
#     print('Excellent')
# elif(80<= marks<90):
#     print('A grade')
# elif(70<= marks<80):
#     print('B Grade')
# elif(60<= marks<70):
#     print('C Grade')
# elif(50<= marks<60):
#     print('D Grade')
# elif(marks<50):
#     print('F Grade you have failed nigga!')



# Problem 7

post = input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")
    
else:
    print("This post is not talking about Harry")