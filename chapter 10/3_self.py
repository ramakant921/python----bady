class Employee:
    language = "Python"
    salary = 1200000
    
    
    def getInfo(self):
        print(f"The language is: {self.language}. \nThe salary is: {self.salary}")
        
    @staticmethod
    def greet(self):
        print("Good Evening niggas!")
    
harry = Employee()
harry.greet()
harry.language = "Javascript" # This is a instance attribute
harry.getInfo()
# Employee.getInfo(harry)