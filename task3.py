#1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float
x=[2,3,4,5,"amit","riyaz","consultadd",2.34,2.56, 1+6j]
print(type(x[-1]))

#2 Create a list of size 5 and execute the slicing structure 
x1=x[:5]
x2=x[2:]
x3=x[3:6]
print(x1, x2,x3)

#3 Write a program to get the sum and multiply of all the items in a given list.
import math
a=[2,3,8,44,5]
a1=sum(a)

def multiply(list):
    result=1
    for i in list:
        result= result*i
    return result
print(a1, multiply(a))    


#4 Find the largest and smallest number from a given list.

print(max(a), min(a))

#5. 	Create a new list which contains the specified numbers after removing the even numbers from a
#  predefined list. 
b=[2,3,4,5,6,7,8,9,10,12,13]
b1=[]
for i in b:
    if(i%2!=0):
        b1.append(i)
print(b1)

#6.	Create a list of first and 
# last 5 elements where the values are square of numbers between 1 and 30 (both included).

c=list(range(1,31))
c1=[]
# c1=c[:6]
# c2=c[26:]
for i in c:
    c1.append(i*i)
print (c1, end=" ")
c2=[c1[:5],c1[25:]]
print(c2)

# Write a program to replace the last element in a list with another list.
d=[[1,3,5,7,9,10],[2,4,6,8]]
d[0][-1:]=d[1][0:]
del(d[1])
print(d)

#Create a new dictionary by concatenating the following two dictionaries:
e={1:10,2:20}
f={3:30,4:40}

e.update(f)
print(e)

#Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
n=int(input("enter a no. "))
g = dict()

for x in range(1,n+1):
    g[x]=x*x

print(g) 

# 10. 	Write a program which accepts a sequence of comma-separated 
# numbers from console and generate a list and a tuple which contains every number.

h=input("enter the no.")
h1= h.split(',')
h2= tuple(h1)
print(h2,h1)









