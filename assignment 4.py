# Task 1: Rectangle class: 
# 1. Write a Rectangle class in Python language, allowing you to build a rectangle 
# with length and width attributes.
# 2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to 
# calculate the area of the rectangle.
# 3. Create a method display() that display the length, width, perimeter and area of an object created 
# using an instantiation on rectangle class.
# 4. Create a Parallelepipede child class inheriting from the Rectangle class and with 
# a height attribute and another Volume() method to calculate the volume of the Parallelepiped

# class rectangle:
#     def __init__(self,length,width) :
#         self.length=length
#         self.width=width

#     def perimeter(self):
#         return 2*(self.length+self.width)

#     def area(self):
#         return self.length*self.width

#     def display(self):
#         print("length", self.length,"\n","width", self.width)
#         print("the perimeter is",self.perimeter())
#         print("the area is",self.area())      


# class parallelepiped(rectangle):
#     def __init__(self,height,length,width):
#         self.height=height 
#         super().__init__(length,width)

#     def volume(self):
#         return self.length*self.width*self.length
    
# length=float(input("please enter length: "))
# width=float(input("please enter width: "))
# height=float(input("please enter height: "))
# obj=parallelepiped(length,width,height)
# obj.display()
# obj.perimeter()
# obj.area()
# print("volume is ",obj.volume())












# Task 2: Person class and child Student class 
# Create a Python class Person with attributes: name and age of type string.
# 1. Create a display() method that displays the name and age of an object created via the Person 
# class.
# 2. Create a child class Student which inherits from the Person class and which also has 
# a section attribute.
# 3. Create a method displayStudent() that displays the name, age and section of an object created 
# via the Student class.
# 4. Create a student object via an instantiation on the Student class and then test the 
# displayStudent method.

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("name: ", self.name)
#         print("age: ",self.age)    

# class student(person):
#     def __init__(self, name, age,section):
#         super().__init__(name, age)   
#         self.section=section  

#     def displaystudent(self):
#         print("name: ", self.name)
#         print("age: ",self.age)
#         print("section: ",self.section)  


# obj = person("raneem", 15)
# obj.display()

# sobj = student("youssef", 20 , "Math")
# sobj.displaystudent() 















# Task 3. Computation class
# Create a Coputation class with a default constructor (without parameters) allowing to perform 
# various calculations on integers numbers.
# 2. Create a method called Factorial() which allows to calculate the factorial of an integer. Test the 
# method by instantiating the class.
# 3. Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. +
# n. Test this method.
# 4. Create a method called testPrim() in the Calculation class to test the primality of a given 
# integer. Test this method.
# 5. Create a method called testPrims() allowing to test if two numbers are prime between them.
# 6. Create a tableMult() method which creates and displays the multiplication table of a given 
# integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 
# 2, 3, ..., 9.
# 7. Create a static listDiv() method that gets all the divisors of a given integer on new list 
# called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given 
# integer

# class computation:
#     def __init__(self) :
#         pass

#     def factorial(self,n):
#         self.n=n
#         j=1
#         for i in range(1,1+n):
#             j=j*i
#         return j   

#     def sum(self,n):
#         j = 1
#         for i in range (1, n + 1):
#             j = j + i
#         return j  
    
#     def testprim(self,n):
#         j=0
#         for i in range(1,n+1):
#             if(n%i==0):
#                 j=j+1
#         if(j==2):
#             return True
#         else:
#             return False
        
#     def testprims(self,n,m):
#         c=0
#         for i in range(1,n+1):
#             if(n%i==0 & m%i==0):
#                 c=+1
#         if c==1:
#             print(n ,m , "  coprime")
#         else: 
#             print(n ,m , "not coprime")  

#     def tablemult(self,x):
#         for i in range (1,10):
#             print (i, "*", x, "=", i * x)

#     def alltables (self):
#         for x in range (1,10):
#             print ("multiplication table of : ", x, "is:")
#             for i in range (1,10):
#                 print (i, "*", x, "=", i * x)   

#     def listdiv(self,n):
#         ldiv = []
#         for i in range (1, n + 1):
#             if (n% i == 0):
#                 ldiv.append (i)
#         return ldiv
   
#     def listdivprim(self,n):
#         ldiv1= []
#         for i in range(1,n+1):
            
#             if (n%i == 0) and (self.testprim(i)):
#                 ldiv1.append(i)          
#         return ldiv1

# x= computation ()
# x.testprims (13, 7)
# a=int(input("to get the list of divisors"))
# b=int(input("to get the list of prime divisors"))
# print ("List of divisors :", x.listdiv (a))
# print ("List of prime divisors :", x.listdivprim (b))
# x.alltables ()



#length of longest commn subsequence       
# def lcs(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif X[m-1] == Y[n-1]:
#         return 1 + lcs(X, Y, m-1, n-1)
#     else:
#         return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
 

# if __name__ == '__main__':
#     S1 = "AGGTAB"
#     S2 = "GXTXAYB"
#     print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))    






        
# def longest_common_subsequence(str1, str2):
#     x = {} 
    
#     def y(i, j):
#         if (i, j) in x:
#             return x[(i, j)]
        
#         if i == len(str1) or j == len(str2):
#             return ''
        
#         if str1[i] == str2[j]:
#             x[(i, j)] = str1[i] + y(i + 1, j + 1)
#         else:
#             option1 = y(i + 1, j)
#             option2 = y(i, j + 1)
            
#             if len(option1) > len(option2):
#                 x[(i, j)] = option1
#             else:
#                 x[(i, j)] = option2
        
#         return x[(i, j)]

#     return y(0, 0)

# str1 = "raneem"
# str2 = "aya"
# result = longest_common_subsequence(str1, str2)
# print(result)    