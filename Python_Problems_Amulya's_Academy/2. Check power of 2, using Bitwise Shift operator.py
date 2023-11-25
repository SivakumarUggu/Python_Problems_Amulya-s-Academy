# 2. Check if a given number is power of 2 or not using Bitwise shift operator.

Num=int(input("Enter any number: "))
i=0
res=0
while res<Num:
    res=1<<i
    if res==Num:
        print('Yes, Given number is power of 2')
        break
    i=i+1
else:
    print("No, Given number is not a power of 2.")



