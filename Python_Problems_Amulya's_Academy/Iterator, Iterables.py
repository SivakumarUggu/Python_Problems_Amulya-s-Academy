# list1=[2,6,1.5,"Hello"]
# iterator=iter(list1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#------------------------------------------------------------------------
#FOR Loop works internally, here we are writing it manually by calling ITER and NEXT Function.

def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item=next(iterator)
        except StopIteration:
            break
        else:
            print(item)

tup=(3,6.5,"Hi")
print_each(tup)




