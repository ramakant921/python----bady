# Problem 1

# name = input("Enter name:")
# marks = int(input("Enter marks: "))
# phone = int(input("Enter phone: "))

# s = "The name of the student is {}, his marks are {} and phone nmmber is {}" .format(name,marks,phone)

# print(s)



# Problem 2

# table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)
# print(s)



# Problem 3

# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False

# a = [1,45,87,4235,657,9867,54,32,54]

# f = list(filter(divisible5,a))
# print(f)



# Problem 4

# from functools import reduce
# l = [1,45,87,4235,657,9867,54,32,54]

# def greater(a,b):
#     if(a>b):
#         return a
#     return b

# print(reduce(greater,l))



# Problem 5

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

app.run()