#Multiple Decorator
# def str_upper(func):
#     def inner():
#         st= func()
#         return st.upper()
#     return inner
#
#
# def str_split(func):
#     def wrapper():
#         str2= func()
#         return str2.split()
#     return wrapper
#
#
# @str_split
# @str_upper
# def str1():
#     return "Hello Everyone"
#
# print(str1())

#---------------------------------------------------------------------------------------------
#Decorator with Parameter

def outer(expr):
    def upper_d(func):
        def inner():
            return func()+expr
        return inner
    return upper_d

@outer(" Amulya")
def print_str():
    return "Good Morning"

print(print_str())

#General Decorator
# def outer(func):
#         def inner(*args):
#             list1=[]
#             list1=args[1:]
#             for i in list1:
#                 if i==0:
#                     return "invalid input"
#             return func(*args)
#         return inner
#
# @outer
# def div1(a,b):
#     return a/b
#
# @outer
# def div2(a,b,c):
#     return a/b/c
#
# print(div1(4,2))
# print(div2(1,2,0))