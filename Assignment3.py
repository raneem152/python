
###################################  Assignment2   ###############################

#1- Implement Fibonacci series using recursion.

# def x(n):
#     if n<=1:
#         return n
#     else:
#         return(x(n-1)+x(n-2))
    
# no_seq = int(input())
# if no_seq <= 0:
#     print("enter a valid number")
# else:
#     for i in range(no_seq):
#         print(x(i))






#2_Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.

# list = ["yes", "no", "hello", "hi","yes","yes", "welcome", "raneem"]
# l1 = []
# count = 0

# for i in list:
#     if i not in l1:
#         count += 1
#         l1.append(i)

# print("list:", l1)
# print("number of unique items:", count)







#3-Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# list=[1,3,4,5,6,7]
# given_value= int(input())
# l1=[]

# for i in  list:
#     for j in list:
#         if i +j == given_value :            
#             l1.append((i,j))

# print(l1)



#4-Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers
# list=[1,2,3,4,5]
# max1=max(list)
# print(max1)
# list.remove(max1)
# max2=max(list)
# print(max2)
# print("the maximum product:",max1*max2)











#5-Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# def prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while n>i:
#         if n % i == 0 and n/n==1:
#             return False
#         i += 1
#     return True
# y=int(input())
# print(prime(y))






#6-Write a Python function to print the even numbers from a given list.
    
# list=[1,2,3,4,5]
# l1=[]
# for i in list:
#     if i%2==0:
#         l1.append(i)
# print(l1)








#7-Write a function that will take a given string and reverse the order of words.

# s = "my name is raneem"
# a = s.split()
# a.reverse()
# print(a)
# x = " ".join(a)
# print(x)








#8-Given an integer x, return true if x is a palindrome, and false otherwise

# def checkPalindrome(n): 
#     for i in range(0, len(n)//2): 
#         if n[i] != str[len(n)-i-1]: 
#             return False
#     return True

# x = input()
# if(checkPalindrome(x) == True): 
#     print("True") 
# else: 
#     print("False")







#9-Write a Python function that checks whether a passed string is a palindrome or not
#can solve problem 8 

# s=input()
# x=s[::-1]
# if x==s:
#     print("palindrome")
# else:
#     print("not palindrome")    









#10-Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included)

# list=list()
# for i in range(1,31):
#     list.append(i**2)
# print(list)    







#11-Write a Python function to generate all permutations of a list.

# def permutation(lst):
#     if len(lst) == 0:
#         return [0]
#     if len(lst) == 1:
#         return [lst]
 
#     l = [] 
#     for i in range(len(lst)):
#        m = lst[i]
#        remLst = lst[:i] + lst[i+1:]
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l

# list=[1,2,3,4,5]
# for p in permutation(list):
#     print (p)








 #12-write a Python program to access a function inside a function

# def f1(): 
#     x = 'raneem' 
#     def f2(): 
#         print(x)    
#     f2() 
# f1() 
