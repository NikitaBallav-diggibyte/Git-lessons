class Student:
    def __init__(self, rno, name, branch):
        self.rno = rno
        self.name = name
        self.branch = branch

    def reading(self):
        print("Roll No:", self.rno)
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Reading...")

    def write(self):
        print("Writing...")

# Creating different student objects
s1 = Student(101, "Amit", "CSE")
s2 = Student(102, "Nikita", "ECE")

# Accessing data
s1.reading()
s1.write()

print()  # Just for spacing

s2.reading()
s2.write()
