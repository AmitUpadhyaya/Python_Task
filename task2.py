# # 1.	Write a program in Python to perform the following operation:
# # If a number is divisible by 3 it should print “Consultadd” as a string
# # If a number is divisible by 5 it should print “c” as a string
# # If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
num=15
if(num%3==0):
    print("Consultadd")

if(num%5==0):
    print("c")

if(num%3==0 and num%5==0):
    print("Consultadd Python Training")  

#-----------------------------------------------------------------------------------------------------------
# #2. 	Write a program in Python to perform the following operator based task:
# # Ask user to choose the following option first:
# # If User Enter 1 - Addition 
# # If User Enter 2 - Subtraction
# # If User Enter 3 - Division
# # If USer Enter 4 - Multiplication
# # If User Enter 5 - Average
# # Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.

x1=[int((input("Enter no 1-"))), int((input("Enter no 2-")))]

sub= str(x1[0]-x1[1])
div= x1[0]/x1[1]
mul= x1[0]*x1[1]
avg= (x1[0]+x1[1])/2
add= int(x1[0]+x1[1])
print(avg)

#------------------------------------------------------------------------------------------------------
# #3 Flow chart

a=int(10)
b=int(20)
c=int(30)

avg= (a+b+c)/3
print("avg=", avg)

if(avg>a and avg>b and avg>c):
    print("avg is higher than a,b,c")

elif(avg>a and avg>b):
    print("Avg is higher than a,b")  

elif(avg>a and avg>b):
    print("avg is higher than a,c")

elif(avg>b and avg>c):
    print("avg is higher than b,c")

elif(avg>a):
    print("avg is higher than a")

elif(avg>b):
    print("avg is higher than b")  

else:
    print("avg is higher than c")

#----------------------------------------------------------------------------------------------------------------
# #  4. 	Write a program in Python to break and continue if the following cases occurs:
# # If user enters a negative number just break the loop and print “It’s Over”
# # If user enters a positive number just continue in the loop and print “Good Going”
    
x3=int(input("Enter a number: "))

while(x3>0):
    print("Good going")
    
print("Its over")    

#--------------------------------------------------------------------------------------------------------------
# 5.   Write a program in Python which will find all such numbers which are divisible  by 7 
# but are not a multiple of 5, between 2000 and 3200.

# x=range(2000,3200)
# if (x%7==0) and (x%5!=0):
#     print (list(x))
l=[]
for x in range(2000, 3200):
    if(x%7==0) and (x%5!=0):
        l.append(str(x))
print(',' . join(l))

#---------------------------------------------------------------------------------------------------------------
# 6What is the output of the following code examples?
# Ans. output would be "int" object is not iterable , object haa to be a list.

x4= [1,2,3]
   	
for i in x4:
   	print(i)

i = 0
while i < 5:
    print(i)

    i += 1
    if i == 3:
        break
else:
    print("error")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
#--------------------------------------------------------------------------------------------------------------
# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#        Expected output: 0 1 2 4 5

for i in range(0,6):  
    if (i==3) or (i==6):
        continue
    print(i, end=" ")

# 8 .  Write a program that accepts a string as an input from user and calculate the number of digits 
# and letters.
# MY approach
# x2= list(input("Enter the input: "))
# for i in range(x2):
#     if (type(x2[i])==str):
#         y2=[x2[i] ]
        
#     else (type(x2[i])==int):
#         y3=[x2[i]]

# print(y2.count(i))

x2= (input("Enter the input: "))
ALpha= digit=0
for i in range(len(x2)):
    if(x2[i].isalpha()):
        ALpha+=1

    else:
        digit+=1
print("letters:", ALpha)
print("digit", digit)
#-----------------------------------------------------------------------------------------------------
#9  Write a program such that it asks users to “guess the lucky number”. 
# If the correct number is guessed the program stops, otherwise it continues forever. 

import random
x1=list(range(0,20))
random_num= random.choice(x1)
while (True):
    y1= int(input("guess the no:"))
    if(random_num==y1):
        print("Good Guess")  
        break
    else:
        print("try again")      

#10 Write a program that asks five times to guess the lucky number. 
# Use a while loop and a counter, such as
import random
x5=list(range(0,10))
random_num= random.choice(x5)
while (True):
    y1= int(input("guess no.1:"))
    y2= int(input("guess no.2:"))
    y3= int(input("guess no.3:"))
    y4= int(input("guess no.4:"))
    y5= int(input("guess no.5:"))
    if(random_num==y1):
        print("Good Guess") 

    elif(random_num==y2):
        print("Good guess") 
    elif(random_num==y3):
        print("Good guess") 
    elif(random_num==y4):
        print("Good guess") 
    elif(random_num==y5):
        print("Good guess") 

    else:
        print("Try again")    

            





    








    

    







    






