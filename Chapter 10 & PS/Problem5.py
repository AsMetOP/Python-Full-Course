from random import randint

class Train:
    def book(self, trainNo, fro, to):
        print(f"Ticket is Booked in train no: {trainNo}, From --> {fro}, To --> {to}") 
    def getStatus(self, trainNo):
        print(f"Train No: {trainNo} is running on time")

    def getFare(self, trainNo, fro, to):
        print(f"Ticket fare for Booked train no: {trainNo}, From --> {fro}, To --> {to} is {randint(222,5555)}")


trainNum = int(input("Enter train number :"))
fro = str(input("From --> "))
to = str(input("To --> "))
details = Train()

details.book(trainNum,fro,to)
details.getStatus(trainNum)
details.getFare(trainNum,fro,to)
