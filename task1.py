#string and operators
#1 Define the string "FUTURA" into a variable and string "LAB" into another variable
#2 print the first and last character of the first string
# a="FUTURA "
# b="LABS"
# print(a[0])
# print(a[5])
#
# #3concatenate two strings into new string
# c=a+b
# print(c)
# #4find length of new string
# print(len(c))
# #5print UTURA LA of the string
# print(c[1:8])
# #6print first 3 character of the string
# print(c[:3])
# #7print the reversal of the string
# c="futuralabs"[::-1]
# print(c)

#8Write a program to create a new string made of the middle three characters of an input string.
# a=input("enter the string:")
# b=a[1:4]
# print(b)

#9)Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# s1=input("enter the first string:")
# s2=input("enter the second string:")
# m=int(len(s1)/2)
# s3=s1[:m:]
# s3=s3+s2
# s3=s3+s1[m:]
# print("After appending new string in middle:", s3)

#10Given string contains a combination of the lower and upper case letters.Write a program to arrange the characters of a string so that all lowercase letters should come first.

# a=input("enter the string:")
# l=[]
# u=[]
# for i in a:
#     if i.islower():
#         l.append(i)
#     else:
#         u.append(i)
#
# b=''.join(l+u)
# print('after rearranging the string:',b)

#11Count all letters, digits, and special symbols from a given string

# a=input("enter your string:")
# c=0
# d=0
# s=0
# for i in a:
#     if i.isalpha():
#         c=c+1
#     elif i.isdigit():
#         d=d+1
#     else:
#         s=s+1
# print("charecters=",c,"Digit=",d,"Symbol=",s)

#12Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

#####LIST AND TUPLE

#1Write a Python program to sum all the items in a list.
# sum=0
# a=[1,2,3]
# for i in a:
#     sum=sum+i
# print(sum)

# 2)Write a Python program to multiply all the items in a list.

# mul=1
# a=[1,2,3,4]
# for i in a:
#     mul=mul*i
# print(mul)

# 3)Write a Python program to convert a tuple to a string.

# a=("kunji","lucky")
# print(type(a))
# b=str(a)
# print(b)


# 4) Write a Python program to convert a list to a tuple

# a=[1,2,3]
# print(type(a))
# b=tuple(a)
# print(b)

#5Python program to interchange first and last elements in a list.

# a=[1,2,3,4,5,6]
# len=len(a)
# b=a[0]
# a[0]=a[len-1]
# a[len-1]=b
# print(a)

#6Python program to find smallest number in a list.

# a=[2,3,4,5]
# print(min(a))

#7Write a python program to print even numbers in a list.

# a=[1,2,3,4,5,6]
# for i in a:
#     if i%2==0:
#         print(i)

#8Write a python program to print odd numbers in a list.

# a=[1,2,3,4,5,6]
# for i in a:
#     if i%2!=0:
#         print(i)

#9Write a python program to print positive numbers in a list..

# a=[1,-1,2,-2]
# for i in a:
#     if i>=0:
#         print(i)

#10Write a python program to print negative numbers in a list.
# a=[1,-1,2,-2]
# for i in a:
#     if i<=0:
#         print(i)

#11Write a python program to covert Fahrenheit to Celsius.




#12Write a python program to print maximum and minimum number in a tuple.

# a=(1,2,3,4,5)
# print("max",max(a),"min",min(a))

#13Write a python program to convert a list into a tuple.

# a=[1,2,3,4,5]
# b=tuple(a)
# print(b)

#14Write a python program to create a list and use the following functions-

# append()
# a=[]
# sum=0
# for i in range(1,5):
#     sum=sum+i
#     a.append(sum)
# print(a)
#extend()

#len()

# a=[1,2,3,4,5]
# print(len(a))

#membership (in, not in)
# a=[1,2,3,4,5]
# i=int(input("enter the number:"))
# if i in a:
#     print("present")
# else:
#     print("not")
