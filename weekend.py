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

for char in b:
    if char in "aeiouAEIOU":
        b1[char]=char

print(b)        



