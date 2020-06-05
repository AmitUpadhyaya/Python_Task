#1.	Create three variables in a single a line and assign different values to them and make sure their
#  data types are different. Like one is int, another one is float and the last one is a string.

x,y,z= int(2),"hi my name is amit", float(2.35)
print(x)
print(type(x))

#2. Create a variable of value type complex and swap it with another variable whose value is an integer.
x1=complex(1+2j)
y1= int(3)
 
temp=x1
x1=y1
y1= temp
print(y1)

#3. Swap two numbers using the third variable as the result name and do the
#  same task without using any third variable.

x2= 5
y2= 8
result= x2
x2= y2
y2= result
print(y2)

x3,y3= 45, 67
x3,y3= y3,x3
print(x3)

#4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.

user= "It is going to rain today"
print(user)

#5 .Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.

x4=int(input("Enter any number 1-10 -"))
y4=int(input("Enter any number 1-10 -"))
z= x4 + y4
print(z)

#Use z for adding 30 into it and print the final result by using variable result.

z+=30
result= z
print(result)

# 6. 	Write a program to check the data type of the entered values.
#  HINT: Printed output should say -  The input value data type is: int/float/string/etc
typ= str(type(z))
print("The input value data type is:" + typ)

#7. If one data type value is assigned to ‘a’ variable and then a different data type value 
# is assigned to ‘a’ again. Will it change the value. If Yes then Why?

# ans. Yes Interpreter will store the latest value in the memory alloted to "a" variable

a= 2
a="hi"
print(type(a))




