#EXAMPLE-1
def outer():
    x=10
    def inner():
        y=5
        result=x+y
        return result
    return inner

a=outer()
print(a())

#Example-2
def outer():
    msg="Hello"
    def inner():
        print(msg)
    return inner

A=outer()
A()
