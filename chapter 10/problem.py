# Problem 1

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
        
        
# p = Programmer("Harry",1200000, 326463)
# print(p.name, p.salary, p.pin, p.company)
# r = Programmer("Rohan",1200000, 326463)
# print(r.name, r.salary, r.pin, r.company)



# Problem 2

# class Calculator:
#     def __init__(self,n):
#         self.n = n
        
#     def square(self):
#         print(f"The square is: {self.n*self.n}")
        
#     def cube(self):
#         print(f"The cube is: {self.n*self.n*self.n}")
        
#     def squareroot(self):
#         print(f"The squareroot is: {self.n**1//2}")
        
        
# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()



# Problem 3

# class Demo:
#     a = 4
    
# o = Demo()
# print(o.a) # Print the class attribute because instance attribute is not present
# o.a = 0  # instance attribute is set
# print(o.a) # Print the Instance attribute because instance attribute is present
# print(Demo.a) # Prints the class attribute



# Problem 4

# class Calculator:
#     def __init__(self,n):
#         self.n = n
        
#     def square(self):
#         print(f"The square is: {self.n*self.n}")
        
#     def cube(self):
#         print(f"The cube is: {self.n*self.n*self.n}")
      
#     def squareroot(self):
#         print(f"The squareroot is: {self.n**1//2}")
        
#     @staticmethod
#     def hello():
#         print("Hello there!")
              
# a = Calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()



# Problem 5

# from random import randint

# class Train:
    
#     def __init__(self,trainNo):
#         self.trainNo = trainNo
    
#     def book(self,  fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
#     def getStatus(self, ):
#         print(f"Ticket no: {self.trainNo} is running on time")
    
#     def getFare(self, fro, to):
#         print(f"Ticket fair in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        
        
# t = Train(5646546)
# t.book("Jupiter","Neptune")
# t.getStatus()
# t.getFare("Jupiter","Neptune")



# Problem 6

# from random import randint

# class Train:
    
#     def __init__(slf,trainNo):
#         slf.trainNo = trainNo
    
#     def book(self,  fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
#     def getStatus(self, ):
#         print(f"Ticket no: {self.trainNo} is running on time")
    
#     def getFare(self, fro, to):
#         print(f"Ticket fair in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        
        
# t = Train(5646546)
# t.book("Jupiter","Neptune")
# t.getStatus()
# t.getFare("Jupiter","Neptune")