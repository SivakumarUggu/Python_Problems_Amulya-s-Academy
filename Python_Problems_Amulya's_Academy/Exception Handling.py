# # #User Defined Exception
# #
# # udict={"nit":"n123"}
# #
# # class loginError(Exception):
# #     def __init__(self):
# #         super().__init__()
# #     def __str__(self):
# #         return "Invaild Uname or Pwd."
# #
# # def login(uname,pwd):
# #      if uname in udict and udict[uname]==pwd:
# #         print("Successfully Login.")
# #      else:
# #         raise loginError()
# #
# #
# # uname=input("Enter username: ")
# # pwd=input("Enter Password: ")
# # try:
# #     print("Resources are open.")
# #     login(uname,pwd)
# # except loginError as e:
# #     print(f"Hi,{e}")
# # else:
# #     print("No Error Occured.")
# # finally:
# #     print("Resources are closed.")
#
# #----------------------------------------------------------------------------------------
# class MultiplyError(Exception):
#     def __init__(self):
#         super().__init__()
#
# def mult(a,b):
#     if a==0 or b==0:
#         raise MultiplyError
#     else:
#         print(a*b)
#
# try:
#     a=int(input("Enter any number: "))
#     b= int(input("Enter any number: "))
#     mult(a,b)
# except MultiplyError:
#     print("Can not multiply number with zero.")

#------------------------------------------------------------------------------------
#RAISE Keyword

try:
    num=int(input("Enter any number: "))
    if num<=0:
        raise ValueError("That is not a positive number.")
except ValueError as error:
    print(error)
else:
    print(f"Entered number is: {num}")
