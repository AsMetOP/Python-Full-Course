class Employee:
    language = "PY"
    salary = 1200000

    def __init__(self, name, salary, language): #Dunder Method --> it automatically calls himself no need to specially call it
        self.name = name
        self.salary = salary
        self.language = language
        print("I am Ironman") 

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod #no need of self
    def greet():
        print("Good Morning")

asmet = Employee("Asmet Sahoo", 1300000, "Java")
print(asmet.name, asmet.language, asmet.salary)
# --> I am Ironman
# --> Asmet Sahoo Java 1300000
asmet.greet() #--> Good Morning
asmet.getInfo() #--> The language is Java and the salary is 1300000
