# Problem 1

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
        
        
# class ThreeDVector:
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
        
#     def show(self):
#         print(f"The vector is {self.i} + {self.j} + {self.k}k")
        
        
# a = TwoDVector(1,2)
# a.show()
# b = ThreeDVector(5,2,3)
# b.show()



# Problem 2

# class Animal:
#     pass

# class Pets(Animal):
#     pass

# class Dog(Pets):
    
#     @staticmethod
#     def bark():
#         print("Bow Bow!")
        
        
# d = Dog()
# d.bark()



# Problem 3

# class Employee:
#     salary = 234
#     increment = 20
#     @property
#     def salaryAfterIncrement(self):
#         return(self.salary + self.salary * (self.increment/100))

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary/self.salary)-1)*100
        

# e = Employee()
# # print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280.8
# print(e.increment)



# Problem 4

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)