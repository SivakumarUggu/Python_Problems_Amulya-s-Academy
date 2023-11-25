#List Comprehensions
# list1=[2,8,1,5,6]
#
# print([x*2 for x in list1])
#
# print([x for x in list1 if x%2==0])
#
# print([x+2 if x%2==0 else x+1 for x in list1])
#
# def square(x):  #Function as expression in LC
#     return x*x
#
# print([square(x) for x in list1])
#
# list2=[9,6,2,4,8]
#
# print([list1[i]+list2[i] for i in range(0,len(list1))])

#--------------------------------------------------------------------------------------------
#Dictionary Comprehension

# fruits=['apple','banana','orange']
# color=['red','yellow','orange']
#
# print({fruit:color for fruit,color in zip(fruits,color)})
# print({fruit:color for fruit,color in zip(fruits,color) if color!='orange'})

#--------------------------------------------------------------------------------------------------
#SET Comprehensions
# list1=[1,2,2,1,3,3,4]
# print({i**2 for i in list1 if i!=3})

#------------------------------------------------------------------------------------------
#Generator Comprehension
list1=[1,2,3]
# def gen_fun(list1):
#     for i in list1:
#         yield i**3
#
# gen_list=gen_fun(list1)
# for j in gen_list:
#     print(j)

my_gen=(i**3 for i in list1)

for i in my_gen:
    print(i)






