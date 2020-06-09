#Create a list of given structure and run 
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:5])
print(x[6],x[7])
print(x[0],x[2],x[4],x[6],x[8])
x.reverse()
print(x)

#6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and 
# print the number which is divisible by 3 and a multiple of 2.
a=list(range(1,100))
print(a)
a1=[]

for i in a:
    if (i%3==0) and (i%2==0):
        a1.append(i)
print(a1) 


b="Hello world" [::-1]
b1=""



print(b)  

# Write a program in Python to iterate through the string 
# “hello my name is abcde” and print the string which has even length of word.

c="hello my name is amit"
c1= c.split(' ')
for i in c1:
    if len(c1)%2==0:
        print(i)

# 9. 	Write a program in python to print the pair of numbers whose sum is equal to
#  result number that is let's say 8.

x=[1,2,3,4,5,6,7,8,9,-1]
x1=8

for i in range(0,10):
    for j in range(i+1, 10):
        if (x[i]+x[j] == x1):
            print(i,j)


# 10. 	Write a program in Python to complete the following task:

# even_list=[]
# odd_list=[]
# d= list(input("Enter no. between 1-50 -"))
# # print(type(d))
# for i in d:
#     if(i%2==0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# print(even_list, odd_list)  

# Write a program to find out the occurrence of a specific word from an alphanumeric statement.

e="1 2 a b c b a c b a b a 3 4 4 a b"
e1= e.split(' ')  
word=str(input("enter letter"))

count= 0

for i in range(0, len(e1)):
    if(word==e1[i]):
        count+=1

print(word,"=", count)   
print(e1)   


# Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tup= (1,2,3,4,5,6,7,8,9,10)
tup1=[]

for i in tup:
    if i%2==0:
        tup1.append(i)
tup2=tuple(tup1)
        
print(tup2)


    




    




