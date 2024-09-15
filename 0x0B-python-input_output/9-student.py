#!/usr/bin/python3
# creating a class Student
class Student:
    #initializing class attributes
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
#public method that retrieves a dictionary representation of the class Student
        
    def to_json(self):

        return{
            "first_name":self.first_name,
            "last_name" :self.last_name,
            "age": self.age
       }
    
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
