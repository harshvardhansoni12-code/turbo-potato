class Task:
    def __init__(self, name, description="student not enrolled"):
        self.name = name
        self.description = description

    def enroll_status(self):
        self.description = "student enrolled"


task = Task("harsh")

print(task.name)
print(task.description)
task.enroll_status()
print(task.description)


''' constructor :- special method of class automatically called 
when object of class is created.'''
class Student:
    def __init__(self, name, age): # __init_ :- constructor of class Student
        # self :- refers to current object of class Student
        self.name = name # instance variable of class Student : value diff for diff obj
        self.age = age
        print("constructor called")
    def check_S(self): # method of class student
        if self.age> 18:
            print("eligible for course")
        else:
            print("not eligible for course")

student_1 = Student("harsh", 22) # this is object of class Student
print(student_1.check_S())                    

# functions defined inside class are called methods.
#  functions defined outside class are called functions available to all classes.

l = [1, 2, 3, 4, 5]
len(l) # this is function available to all classes.
# It is not a method of class list.

l.append(6) # this is a method of class list.

