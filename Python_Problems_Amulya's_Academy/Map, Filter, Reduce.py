# #MAP
# def add(a):
#     return a+a
#
# numbers=[2,3,4,5]
#
# output=map(add,numbers)
# sum=list(output)
# print(sum)
#
# #------------------------------------------------------------
#
# string=['jenny','rockey','jack']
# res=map(str.upper, string)
# print(list(res))
# #------------------------------------------------------------
#
# result=map(lambda word:len(word), string)
# print(list(result))
# #---------------------------------------------------------------------------------------
# Filter
# def fil(num):
#     return num>5
#
# number=[3,8,1,6,9]
# res1=filter(fil, number)
# print(list(res1))
#
# res2=filter(lambda x:x%3==0, number)
# print(list(res2))
#
# def veggies(x):
#     return 'e' in x
#
# veg=['ginger','garlic','soda']
#
# res3=filter(veggies, veg)
# print(list(res3))
# #---------------------------------------------------------------------------------------
#Reduce
from functools import reduce
def sum(a,b):
    return a+b
li=[1,2,3,4]
sum_nums=reduce(sum, li)
print(sum_nums)

result=reduce(lambda a,b:a*b, li)
print(result)
#
