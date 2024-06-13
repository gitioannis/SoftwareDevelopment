

class Customer:
    def __init__(self, Id, name, email, age):
        self.Id = Id
        self.name = name
        self.email = email
        self.age = age
    
    def __str__(self):
        return f"Customer ID: {self.Id}, \nName: {self.name}, \nAge: {self.age}, \nEmail: {self.email}"
    
    def updateEmail(self, newEmail):
        self.email = newEmail
    
customer1 = Customer(1, "John Doe", "john.doe@example.com",50)
customer1.updateEmail('jdoe@example.com')

# Inheritance: Employee behaves as customer with jobpost and salary
class Employee(Customer):
    def __init__(self,Id,name,email,age,jobpost,salary):
        super().__init__(Id,name,email,age)
        self.jobpost = jobpost
        self.salary = salary
    
    def NICont(self):
        niCont = self.salary * 0.08
        return f"NI Contributions: {niCont}"
        
    def TaxAmount(self):
        tax = self.salary * 0.20
        return f"Taxable Amount: {tax}"
    
    def __str__(self):
        return f"Customer ID: {self.Id}, \nName: {self.name}, \nAge: {self.age}, \nEmail: {self.email}, \nJob Post: {self.jobpost}, \nSalary: {self.salary}"


employee1 = Employee(1000,'Julian Smith','jsmith.company.net',30,'Management',45000)
employee1.updateEmail('julsmith.company.net')

print(customer1,"\n")
print(employee1)
print(employee1.NICont())
print(employee1.TaxAmount())
        
    