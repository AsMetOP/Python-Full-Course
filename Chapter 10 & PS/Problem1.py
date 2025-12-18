class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Asmet", 120000, 753008)
print(f"Company : {p.company}, Name: {p.name},Salary: {p.salary},Pincode: {p.pincode}")
r = Programmer("Rohan", 120000, 753008)
print(f"Company : {r.company}, Name: {r.name},Salary: {r.salary},Pincode: {r.pincode}")