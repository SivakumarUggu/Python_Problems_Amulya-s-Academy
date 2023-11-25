from datetime import *

# d=date(2021,12,31)
# print(d)
# print(d.day)
# print(d.month)
# print(d.year)

# n=int(input("Enter number of students: "))
# stud={}
# for i in range(1,n+1):
#     rollno=int(input("rollno: "))
#     name=input("enter name: ")
#     doj=date.fromisoformat(input("Enter date:"))
#     stud[i]=[rollno,name,doj]
#
# print(stud)

# import datetime
#
# date_str = "2023-11-24"
# date_object = datetime.date.fromisoformat(date_str)
#
# print(date_object)


# list1=[['ram',date(2022,1,28)],['krish',date(2015,9,27)] ]
# for stud in list1:
#     name,d=stud
#     if d.month==9:
#        print(name)

# print(date.today())
#
# timeobj=time()
# print(timeobj)
#
# timeobj2=time(5,9,30)
# print(timeobj2)

# t1=time.fromisoformat('12:30:20')
# print(t1)

#TIMEDELTA Class or DataType
d1=date(2022,12,3)
print(d1)
td=timedelta(days=10)
d1=d1+td
print(d1)
d1=d1-td
print(d1)
weeks=timedelta(weeks=4)
d1=d1+weeks
print(d1)
