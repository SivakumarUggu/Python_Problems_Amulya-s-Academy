#Passing Function as a Parameter to another function.
# def fun1():
#     print("Hi, I am from function1.")
#
# def fun2(func):
#     print("Hi, I am function 2, now i will call function-1")
#     func()
#
#
# fun2(fun1)
#----------------------------------------------------------------------------------
#Decorators-1

# def str_upper(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner
#
# @str_upper
# def print_str():
#     return "Hello, Pythonistas"
#
# print(print_str())

#-------------------------------------------------------------------------------
def zerodiv_deco(func):
    def inner(x,y):
        if y==0:
            return "Enter proper input."
        return func(x,y)
    return inner



@zerodiv_deco
def div(a,b):
    return a/b

print(div(4,0))

