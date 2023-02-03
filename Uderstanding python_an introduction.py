#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Arithmetic operators


# In[2]:


5+3


# In[3]:


10%3


# In[4]:


10//3


# In[5]:


4*(2/5*7)**2


# In[6]:


2*((21/5)-(2/4))**2


# In[3]:


a=(7-4)*((343**2/3)/49**-1/3)
print(a)


# In[4]:


type(a)


# In[8]:


#assignment operators


# In[9]:


a =8
b = 6
c = a+b
d = a+b+c


# In[10]:


print(c)


# In[11]:


b*a


# In[12]:


print(d)


# In[13]:


#concantination


# In[6]:


a= 'pat'
b= ' '
c= 'favor'
d = a+b+c
print(d)


# In[15]:


a="this is my book"
b =","
c ="i bought it yesterday"
d= a+b+c


# In[16]:


print(d)


# In[17]:


a="this the girl "


# In[18]:


b=","
c="that gave me the bag"
d=a+b+c


# In[19]:


print(d)


# In[20]:


#if and elif


# In[21]:


x=10
y=15
if x==y:
    print("x is equal to y")
elif x<y:
    print("x is less than y")
else:
    print("x is greater than y")


# In[22]:


username = "sam"
password = 123
if username=="sam" and password==1234:
    print("welcome")
else:
    print("wrong password")


# In[23]:


type (password)


# In[24]:


marks =70
if marks>=70:
    print ("a")
elif marks>=60:
    print ("b")


# In[25]:


#python loop


# In[26]:


n=1
while n<=20:
    print(n)
    n +=1


# In[1]:


p=1
while p<=20:
    print(p)
    if p==15:
        break
    p +=1


# In[28]:


#borleans


# In[29]:


t = True
f = False
print(t and f)
print(t or f)


# In[30]:


a=True
b= False
c= True
d = False
print(a and b)
print(a and c)
print(a and d)
print(b and c)
print(b and d)


# In[31]:


print (a or b)
print (a or c)
print (a or d)
print (b or c)
print (b or d)


# In[32]:


#input parameters


# In[33]:


Name= input('enter your name')


# In[34]:


print("hello", Name, 'you are welcome')


# In[35]:


#slicing and indexing


# ###### indexing

# In[36]:


x='hello'


# In[37]:


x[1]


# In[38]:


x.index("h")


# #### slicing

# In[39]:


a=2,5,4,9,0,3,10


# In[40]:


a[:4]


# In[41]:


a[0:]


# In[42]:


a[2:6]


# In[43]:



get_ipython().run_line_magic('pinfo', 'divmod')


# In[44]:


divmod(34,5)


# In[45]:


isinstance(1,int)


# In[46]:


isinstance(1.6,int)


# In[47]:


isinstance(1.6,(int,float))


# In[48]:


isinstance(1+5j,(int,float,complex))


# In[49]:


isinstance(1+5j,(int,float,bool,str))


# In[50]:


p=6/2j
type(p)


# In[51]:


pow(4,2)


# In[52]:


d=5
f=5
pow(d,f)


# In[53]:


5**5


# In[54]:


pow(4,2,5)
"""this will give the result of 4**2%5
"""


# In[55]:


int(input("enter an intigar"))


# In[56]:


a=int(input())
b=int(input())
if a>b:
    print(a)
    print("a is greater than b")
print("outside the if condition")


# In[57]:


x=float(input())
y=round(x)
if x>0:
    if y>x:
        intportion=y-1
    else:
        intportion=y
else:
    if y<x:
        intportion=y+1
    else:
        intportion=y
            
if intportion%2==0:
            print("Even")
else:
    print("Odd")


# In[2]:


n=int(input())
i=1
while (i < n):
    print(i)
    i+=1
print ("don")


# In[59]:


n=int(input('max iteration ='))
i=1
while (i < n):
    print(i**2)
    i+=1
print ("don")


# In[60]:


m= int(input('max iteration ='))
j=1
while j<m:
    if j%2==0:
        print(j)
    else:
        pass
    j+=1


# In[61]:


l=[]
for i in range(10):
    print(i+1)
    l.append(i**2)
print(l)


# In[62]:


l=[]
for i in range(0,10,2):
    print(i+1)
    l.append(i**2)
print(l)


# In[63]:


L=[1,2,4,-5,6,5,9,10,14,-2]
m=L[0]
idx=0
c=0
for i in L:
    if i<m:
        m=i
        idx=c
    c+=1
tmp=L[0]
L[0]=m
L[idx]=tmp


# In[64]:


L


# In[65]:


L=[1,2,4,-5,6,5,9,10,14,-2]
for j in range(len(L)):
    m=L[j]
    idx=j
    c=j
    for i in range(j,len(L)):
        if L[i]<m:
            m=L[i]
            idx=c
        c+=1
    tmp=L[j]
    L[j]=m
    L[idx]=tmp
print(L)


# In[66]:


def msg(entry):
    """function prints the entry supplied by the user or alerts that the entry is not of the the expected data type
    """
    if isinstance(entry,str):
        print(entry)
    else:
        print("Your entry is not of the expected data type")
        print("Here is the  data type of what you supplied",type(entry))


# In[67]:


help(msg)


# In[68]:


get_ipython().run_line_magic('pinfo2', 'msg')


# In[69]:


msg('I am becoming better with data analysis in python every day')


# In[70]:


msg(12)


# In[71]:


def Add(*args):
    Total=0
    for i in range(len(args)):
                   Total+=args[i]
    return Total


# In[72]:


print(Add(8,5,323,7,25,70,3,1))


# In[73]:


def printvariablesnamesandvalues(**args):
    for x in args:
        print("variables names is :", x,"and its value is:",args[x])


# In[74]:


printvariablesnamesandvalues(a=3,b='B', C='T',D = 7)


# In[1]:


def h(s=6):
    print(s)


# In[2]:


h(5)


# In[76]:


h(45)


# In[77]:


import sys
sys.path.append('C:/functions/')


# In[78]:


import my_function_collection as mfc 


# In[3]:


print("i'm learning \"string\" at the moment")


# In[4]:


print("we are learning 'data science' with jupyter notebook")


# In[6]:


print("i'm still learning. \n Are you too?")


# In[6]:


"""you want to enter all your students records in a computer and compute the
avrage marks of each student"""
def getDataFromUser():
    D={}
    while True:
        studentId = input("input student ID: ")
        marksList = input("input the marks by CSV: ")
        moreStudents = input("input yes/no for adding students: ")
        if studentId in D:
            print(studentId, "is already entered")
        else:
            D[studentId] = marksList.split(",")
            if moreStudent.lower()=="no":
                return D
            


# In[79]:


from scipy import stats


# In[80]:


speed = [25,43,46,77,33,54,22,12,22,34,12,55,54,12,12,23,77]
stats.mode(speed)


# In[81]:


import numpy as np
np.mean(speed)


# In[82]:


np.median(speed)


# In[83]:


np.std(speed)


# In[84]:


np.var(speed)


# In[85]:


percentile=np.percentile(speed,60)
print(percentile) #gives a number that desscribes the value that a given percent of the values are lower than


# In[86]:


unidata=np.random.uniform(0.0,5.0,250)
print(unidata)


# In[87]:


from matplotlib import pyplot as plt


# In[88]:


plt.hist(unidata,5)
plt.show()


# In[89]:


normaldata= np.random.normal(5.0,1.0,100000)
plt.hist(normaldata,100)


# In[90]:


x=np.random.normal(5.0,1.0,1000)
y=np.random.normal(10.0,2.0,1000)
plt.scatter(x,y)
plt.show()


# In[92]:


age = [5,6,7,9,10,12,8,14,2,1,1,3]
speed2 = [78,60,56,47,45,40,48,34,90,92,95,80]
plt.scatter(age,speed2)
plt.show()


# In[99]:


age = [5,6,7,9,10,12,8,14,2,1,1,3]
speed2 = [78,60,56,47,45,40,48,34,90,92,95,80]

slope,intercept,r,p,std_err=stats.linregress(age,speed2)
def myfunction(age):
    return slope * age + intercept

myModel= list(map(myfunction,age))

plt.scatter(age,speed2)
plt.plot(age,myModel)
plt.show()

print(r) # (r-squared)used to measure the relationship between the x and y variables. it ranges from 0 to 1, 0 = no relationship, 1=100% related
predict=myfunction(11) #used to predict future values
print(predict)
print('-0.97 indicates a weak relationship but we can use the relationship to predict future values')


# In[117]:


x=[1,2,3,5,6,7,9,10,11,12,14,15,16,18,19,21,22]
y=[100,90,90,80,70,60,60,50,40,30,30,30,30,20,10, 10,100]

myModel=np.poly1d(np.polyfit(x,y,3))

myline=np.linspace(1,22,100)

plt.scatter(x,y)

plt.plot(myline,myModel(myline))

plt.show()

print('the polynomial regression of x and y')

from sklearn.metrics import r2_score #sklearn.metrics is the modle used to calculate the  R-square value for polynomial regression

print(r2_score(y,myModel(x)))

print('there is a strong relationship between x and y')
speedpredict=myModel(20)
print(speedpredict)


# In[ ]:




