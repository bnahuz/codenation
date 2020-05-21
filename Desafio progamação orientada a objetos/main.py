class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee():
    def __new__(cls, code, name, salary):
        if cls is Employee:
            raise TypeError("Employee may not be instantiated")
        return object.__new__(cls)

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
    
    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self.__departament.name
    
    def set_departament(self, name, code):
        self.__departament = Department(name, code)


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_departament(self):
        return self.__departament.name
    
    def set_departament(self, name, code):
        self.__departament = Department(name, code)

    def get_sales(self):
        return self.__sales

    def put_sales(self,unique_sales):
        self.__sales += unique_sales

    def calc_bonus(self):
        return self.get_sales() * 0.15

breno = Manager(123,'Breno', 500)

print(breno.salary)
print(breno.calc_bonus())