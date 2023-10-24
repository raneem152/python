#!/usr/bin/env python
# coding: utf-8

# In[11]:


tuple = (1, 2, 3)
x=input()
 
newtuple = tuple + (x,)
print(newtuple)


# In[13]:


list = [1,2,3,4,5]
sum=0
for i in range(0, len(list)):
    sum = sum + list[i]
print(sum)


# In[18]:


list = [1,2,3,4,5]
mul=1
for i in range(0, len(list)):
    mul = mul *list[i]
print(mul)


# In[21]:


list = [61,2,3,4,5]

list.sort()
print(list[0])
        


# In[22]:


list = [61,2,3,4,5]

list.sort()
print(list[-1])
        


# In[27]:


# define string
string = "raneem aya hi hello 3aaaaaa"
x = " "


count =1
y=string.count(x)

# print count
print("there are ",y+1,"strings")


# In[30]:


list = ["raneem", "aya", "toka"]
copied = list.copy()
print(copied)
#print (list)


# In[33]:


list = ["raneem", "aya", "toka","youssef"]
list.remove("aya") #or discard far2 bas an law est5demt remove haga w hya msh mawgoda fy al list 7ydeny error
print(list)


# In[34]:


x = {1, 2, 3, 4, 5} 
y = {4, 5} 
print(y.issubset(x))


# In[35]:


set={1, 2, 3, 4, 5} 
set.clear()
print(set)


# In[36]:


set={1, 2, 3, 4, 5} 
print(min(set))
print(max(set))


# In[38]:


Tuple = ( 1, 3, 4, 2, 5, 6 )
res = Tuple.index(1)
print(res)


# In[45]:


tup1 = ('raneem', 'aya', 'toka')
tup2 = (1, 2, 3)
res = {}
for i in range(len(tup1)):
    res[tup1[i]] = tup2[i]
print(res)


# In[51]:


list = [('raneem', 1), ('aya', 2), ('toka', 3), ('youssef', 4)]
 

res = [[i for i, j in list],
       [j for i, j in list]]
print(res)


# In[53]:


tuple = ('1','2','3','4','5','6','7','8')
newtuple = tuple[::-1]
print(newtuple)


# 

# In[69]:


tups = [('raneem', 1), ('aya', 2), ('toka', 3), ('youssef', 4)]
dictionary = {}
for i, j in tups:
    dictionary.setdefault(i, j)
print(dictionary)


# In[72]:


l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
x=[i[:-1] + (11111,) for i in l]
print(x)


# In[79]:


class student():
    count=0 
    def __init__(self,name,age,number):
        
        name=self.name
        age=self.age
        number=self.number
        student.count=student.count+1

        student1=student("raneem" , 23,5)
        student2=student("raneema" , 22,54)
        student3=student("raneemo" , 21,6)

        print (student.count)
        print (student1.name)
        print (student2.age)
        print (student3.number)


# In[ ]:




