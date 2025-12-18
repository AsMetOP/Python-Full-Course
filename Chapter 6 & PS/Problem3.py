p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click this"

message = str(input("Enter your comment:"))

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Spam Comments")

else: 
    print("Not a spam")
    print("Thankyou! Bhai")