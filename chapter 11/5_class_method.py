class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class vattribute of a is{cls.a}")
        
e = Employee()
e.a = 45

e.show()