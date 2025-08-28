# Problem 1

# a = 3
# b = 78
# c = 9

# def greatest (a,b,c):
#     if(a>b and a>c):
#         return a
#     if(b>a and b>c):
#         return b
#     if(c>b and c>a):
#         return c
    
    
# a = 3
# b = 78
# c = 9

# print(greatest(a,b,c))



# Problem 2


# def f_to_c (f):
#     return 5*(f-32)//9
    
# f = int(input("Enter temperature in F: "))
# print(f"{f_to_c(f)}°C")



# Problem 3

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")



# Problem 4

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + 1

# print(sum(4))



# Problem 5

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)
    
# pattern(75)



# Problem 6

# def inch_to_cms(inch):
    # return inch*2.54

# n = int(input("Enter the value in inch: "))
 
# print(f"The corresponding value of cm is {inch_to_cms(n)}")       



# Problem 7

def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n
    

l = ["Veriton", "Harrison", "Vidya"]

print(rem(l, "n"))

