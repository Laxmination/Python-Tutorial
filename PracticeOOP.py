class Book: #Book is class here
    name = "Harry Potter"
    writer = "J.K Rowling"

book1 = Book() #book1 is object here
print(book1.name) # name is attribute here
print(book1.writer) # writer is an attribute here 


class X: # X is class here
    value = 10
    position = "x-axis"

x1 = X() # x1 is object here 
print(x1.value) #value is an attribute here 
print(x1.position)

class Student:
    def __init__(self, fullName, rollno):  # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self.name = fullName
        self.rollno = rollno
        # print(self)
        print("Database of class student")

s1 =Student("Sai Pallavi", 10)
print(s1.name)
print(s1.rollno)
