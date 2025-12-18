class Employee:
    language = "PY"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod #no need of self
    def greet():
        print("Good Morning")

asmet = Employee()
asmet.name = "Asmet Sahoo"
asmet.language = "Java"
print(asmet.name, asmet.language, asmet.salary)

asmet.getInfo()
asmet.greet()
#Employee.getInfo(asmet)