# THIS IS A SIMPLE CALCULATOR TO LEARN DEVELOP SOME BASIC PROGRAM



def add(num1,num2):
    return num1+num2
    
def sub (num1,num2):
    return num1-num2
    
def multiply (num1,num2):  
    return num1*num2 
    
def division (num1,num2):
    return num1/num2

print("Please select opertors: +,-,*,/")

operators = input("Select opertor: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (operators == "+"):
    print(num1,"+",num2,"=",add(num1,num2))
    
    
elif (operators == "-"):
    print(num1,"-",num2,"=",sub(num1,num2))
    
    
elif (operators == "*"):
    print(num1,"*",num2,"=",multiply(num1,num2))
    
    
elif (operators == "/"):
    print(num1,"/",num2,"=",division(num1,num2))
    
else:
    print("Noob tumhe toh calculator chalane bhi nahi aati🤣🤣")