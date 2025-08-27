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


def f_to_c (f):
    return 5*(f-32)//9
    
f = int(input("Enter temperature in F: "))
print(f"{f_to_c(f)}°C")