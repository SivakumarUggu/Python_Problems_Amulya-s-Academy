#1. Print non_empty substrings of given string.

str1=input("Enter any string: ")
for i in range(0,len(str1)):
        for j in range(i+1,len(str1)+1):
              print(str1[i:j], end=" ")
        print()

