# x=10
# def fun():
#     y=5
#     global x
#     x=x+1
#     print("Y is: ", y)
#     print("Inside the function X is: ", x)
#
# fun()
# print(x)
#---------------------------------------------------------------------------------------
#Enclosed Variable

# x=15
# def outer():
#     y=10
#     def inner():
#         z=5
#         nonlocal y
#         y=y+3
#         print("Z is: ", z)
#         print("Inside the inner fn Y is: ", y)
#     inner()
#     print(y)
#
# outer()

#---------------------------------------------------------------------------------

#LEGB Rule (Order of Execution)
#x=10      #-----------Third Global scope
def function():
    x=15   #---------Second- Enclosed Scope
    def inner():
        # x=20 -----First- Local Scope
        print("X is:",x)
    inner()
function()       




