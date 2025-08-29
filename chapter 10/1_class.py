class Employee:
    name = "Harrison"
    language = "py" #this is a class attribute
    salary = 1200000
    
harry = Employee()
harry.name = "Harry" #this is a object attribute
print(harry.name,harry.language)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object attribute and salary and language are class atrribute as they directly belong to the class