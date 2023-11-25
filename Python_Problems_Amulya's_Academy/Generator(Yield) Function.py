def fib(mymax):
    a,b=0,1
    while True:
        c=a+b
        if c<mymax:
            print("Before Yield.")
            yield c
            print("After Yield.")
            a,b=b,c
        else:
            break

Gen=fib(14)
for i in Gen:
    print(i)

# print(next(Gen))
# print(next(Gen))
# print(next(Gen))