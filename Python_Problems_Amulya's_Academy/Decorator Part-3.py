#getting original function name
# import functools
# def deco(func):
#     @functools.wraps(func)
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner
#
# @deco
# def greet():
#     return "Good Morning"
#
# print(greet.__name__)

#-------------------------------------------------------------------------------------
#Applying deco on class method
# def decorator(method):
#     def inner(obj_ref):
#         if obj_ref.name=="Joya":
#             print(f"Hey, My name is also same.")
#         else:
#             method(obj_ref)
#     return inner
#
#
# class deco:
#     def __init__(self,name):
#         self.name=name
#
#     @decorator
#     def print_str(self):
#         print(f"Entered name is:, {self.name}")
#
# P=deco("Soya")
# P.print_str()

#----------------------------------------------------------------------------------------
#__CALL__ Method
# class printing:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print("Hello, Everyone")
#
# P=printing("Ria")
# P()

#-------------------------------------------------------------------------------------------
#CLASS Decorator
# class Decorator:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self):
#         str1=self.func()
#         return str1.upper()
#
# @Decorator
# def greet():
#     return "Good Morning"
#
# print(greet())

#----------------------------------------------------------------------------------------
#
class check_div:
    def __init__(self,func):
          self.func=func
    def __call__(self, *args, **kwargs):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return "can not divide with zero."
            else:
                return self.func(*args,**kwargs)


@check_div
def div(a,b):
    return a/b
@check_div
def div1(a,b,c):
    return a/b/c

print(div(18,9))
print(div1(3,6,2))







