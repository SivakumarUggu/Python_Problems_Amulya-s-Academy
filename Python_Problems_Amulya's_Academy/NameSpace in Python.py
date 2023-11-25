print("\nInitially: ", dir())
num=20

def fun():
    n=10
    print("\nInside the function: ", dir(),'\n')
fun()
print("Outside the function: ", dir())