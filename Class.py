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
customer2 = Customer(2, "Maria Kallas", "maria.kallas@example.com",108)

print("Original data:")
print(customer1)
customer1.updateEmail("jdoe@example.com")
print("Modified data:")
print(customer1)
print('-'*20)

print("Create a customers list and loop through")
customers = [customer1, customer2]
for customer in customers:
    print(customer)
    print('-'*10)