#Instance Variables and Class variables

# class Student:
#     clg_name="XYZ"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def msg(self):
#         return (self.name + " age is " + self.age)
#
# s1=Student("amulya",'22')
# print(s1.name)
# print(s1.age)
# print(s1.clg_name)
# print(Student.clg_name)
# print(s1.msg())

#------------------------------------------------------------------------------
# Count the number of objects
# class Student:
#     counter=0
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         Student.counter+=1
#
#     def msg(self):
#         return (self.name + " got " + self.marks)
#
#     @classmethod
#     def obj_count(cls):
#         return cls.counter
#
# s1=Student("ria", 95)
# s2=Student("chaaya",98)
# s3=Student("meera", 90)
# print(s1.obj_count())
# print(Student.obj_count())

#----------------------------------------------------------------------------------------
# Convert total marks into percentage
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def msg(self):
#         print(self.name + " got " + self.marks,'%')
#
#     @classmethod
#     def get_per(cls,name,marks):
#         return cls(name, str((int(marks)/600)*100))
#
# # s1=Student("sia","95")
# # s1.msg()
# name="jane"
# marks="450"
# s2=Student.get_per(name,marks)
# s2.msg()

#---------------------------------------------------------------------------------------------
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def msg(self):
        print(self.name + " got " + self.marks,'%')

    @classmethod
    def get_per(cls,name,marks):
        return cls(name, str((int(marks)/600)*100))

    @staticmethod
    def get_age(age):
        if age<17:
            print("Belongs to school")
        else:
            print("Do not belongs to school")

s1=Student.get_per("Tim","450")
s1.msg()
Student.get_age(15)
