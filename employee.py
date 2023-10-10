"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalariedEmployee(Employee):
    def __init__(self, name, salary, commissionType="NONE", commission=0, contracts=0):
        self.name = name
        self.salary = salary
        self.commissionType = commissionType.upper()
        self.commission = commission
        self.contracts = contracts
    
    def get_pay(self):
        if self.commissionType == "BONUS":
            return self.salary + self.commission
        elif self.commissionType == "CONTRACT":
            return self.salary + (self.commission * self.contracts)
        else:
            return self.salary
        

    def __str__(self):
        if self.commissionType == "BONUS":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        elif self.commissionType == "CONTRACT":
            return f"{self.name} woeks on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}"
        else:
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, wage, hours, commissionType="NONE", commission=0, contracts=0):
        self.name = name
        self.wage = wage
        self.hours = hours
        self.commissionType = commissionType.upper()
        self.commission = commission
        self.contracts = contracts
    
    def get_pay(self):
        if self.commissionType == "BONUS":
            return (self.wage * self.hours) + self.commission
        elif self.commissionType == "CONTRACT":
            return (self.wage * self.hours) + (self.commission * self.contracts)
        else:
            return self.wage * self.hours
        
    def __str__(self):
        if self.commissionType == "BONUS":
            return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        elif self.commissionType == "CONTRACT":
            return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}"
        elif self.commissionType == "NONE":
            return f"{self.name} works on contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalariedEmployee('Renee', 3000, "CONTRACT", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 25, 150, "CONTRACT", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedEmployee('Robbie', 2000, "BONUS", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 30, 120, "BONUS", 600)