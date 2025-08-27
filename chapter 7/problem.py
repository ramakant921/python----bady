# Problem 1

# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*1}")
  
  
    
    # Problem 2
        
# l = ["Harrison","Soham","Sammer"]
# for name in l:    
#     if(name.startswith("S")):
#         print(f"Hello {name}!")


    
    # Problem 3
    
# n = int(input("Enter a number: "))

# i = 1

# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i+=1



#  Problem 4

# n = int(input("Enter a number: "))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime number")



#  Problem 5

# n = int(input("Enter the number: "))
# i = 0
# sum = 0

# while(i<n):
#     sum += 1
#     i+=1
    
# print(sum)



# Problem 6

# n = int(input("Enter the number: "))
# product = 1
# for i in range(1,n+1):
#     product = product*i

# print(f"The factorial of {n} is {product}")



# Problem 7

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*" * ((2*i)-1), end="")
#     print("")



# Problem 8

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     if( i==1 or i==n):
#         print("*"* n,end="")
#     else:
#         print("*", end= "")
#         print(" "* (n-2), end= "")
#         print("*", end= "")
#     print("")



# Problem 9

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    i += 1