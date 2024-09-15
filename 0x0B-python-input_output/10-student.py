#!/usr/bin/python3
# creating a class Student
class Student:
    #initializing class attributes
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
#public method that retrieves a dictionary representation of the class Student
        
    def to_json(self,attrs=None):
        if attrs and isinstance(attrs,list):
            result = {}
            for attr in attrs:
                if isinstance(attr,str) and hasattr(self,attr):
                    result[attr] = getattr(self,attr)
            return result


        return{
            "first_name":self.first_name,
            "last_name" :self.last_name,
            "age": self.age
       }
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
  