class Student:
    rno= 123   # class variable
    name="abc" # class variable
    branch= "cse" # class variable
    def reading(self):
        rno= 456 # local variable
        print("rno", rno) #  It will print 456, high preference than class variable
        print("class variable", self.rno)  # It will print 123
        print ("reading.....")
    def write(self):
        print("Writing.....")

abc = Student()   #object1
obj = Student()   # object2
print("rno", Student.rno)  #printing variable
print("name", abc.name)
print("branch", abc.branch)
abc.reading() # calling function
abc.write()
print("name", obj.name)