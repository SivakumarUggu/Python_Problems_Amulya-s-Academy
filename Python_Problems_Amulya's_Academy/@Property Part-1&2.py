# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#
#     @property
#     def msg(self):
#         return self.name + " got grade " + self.grade
#
#     @msg.setter
#     def msg(self,msg):
#         sent=msg.split(" ")
#         print(sent)
#         self.name=sent[0]
#         self.grade=sent[-1]
#
#
#
# stud=Student("Roopa",'B')
# print(stud.msg)
#
# stud.msg="Amulya got grade A"
# print("name: ", stud.name)
# print("Grade: ", stud.grade)
# print(stud.msg)
#
# #-----------------------------------------------------------------------------------
# # @Property Part-2
class Student:
    def __init__(self,marks):
        self.__marks=marks

    def per(self):
        return (self.__marks/600)*100

    def setter(self,value):
        if value<0 or value>600:
            print("Can not set the value, stick to previous value.")
        else:
            print("Setting Vlaue: ",value)
            self.__marks=value

    def getter(self):
        print("Getting Value: ", end=' ')
        return self.__marks
    marks=property(getter,setter)

stud=Student(400)
stud.marks=500
print(stud.marks)
print("%.4f"%stud.per(),'%')






