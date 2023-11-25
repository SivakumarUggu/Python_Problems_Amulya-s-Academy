numbers=[3,6,9]
res=all(num%3==0 for num in numbers)
print(res)

numbers=[6,1,5,7]
res=any(num%3==0 for num in numbers)
print(res)