#Write a program to reverse a string.

def reverse(str):
    s=str[::-1]
    return(s)

print(reverse("amit"))

# Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.

def case(str):
    uppercase=0
    lowercase =0
    
    for c in str:
        if c.isupper():
           uppercase+=1
        elif c.islower():
           lowercase+=1
        else:
           pass
    print("No of uppercase character: ",uppercase)
    print("No of uppercase character: ",lowercase)
    
case("hi MY Name IS Amit")

# 3.  Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_elements(list):
  x = []
  for i in list:
    if i not in x:
      x.append(i)
  return x

print(unique_elements([6,6,5,5,8,8,9,9,"amit","amit"]))  

# 4.         Write a program that accepts a hyphen-separated sequence of words as input and prints the
#  words in a hyphen-separated sequence after sorting them alphabetically.

# def Sep(arg):
#     c=[]
#     c1=c.split('-')
#     c1.sort()
#     for i in arg:
#         c.append(i)
      
#     return c1
# print(Sep("Hello amit" )

# 5.  Write a program that accepts a sequence of lines as input and 
# prints the lines after making all characters in the sentence capitalized.

def capital(arg):
    d= []
    for i in arg:
        d.append(i.upper())
    return d
print(capital("wellsfargo"))        

# 6.    Define a function that can receive two integral 
# numbers in string form and compute their sum and print it in console.

def int_num(arg1,arg2):
     x= int(arg1)
     y= int(arg2)
     z= x+y
     print(z)
int_num("2","3")


#7 Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line
def str_length(arg1, arg2):
    y1= arg1
    y2= arg2

    if (len(y1)==(len(y2))):
        print(y1)
        print(y2) 
    else:
        print("length y1", len(y1), "length y2", len(y2))  
str_length("amit", "riyaz")   
str_length("world", "india" )      

#8. Define a function which can generate and print a tuple where the 
# value are square of numbers between 1 and 20.

def tup_sq(arg):
    l=[]
    for i in arg:
        l.append(i*i)
    print(tuple(l))    
      
tup_sq([2,3,4,5])

#9 Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 

def showNumbers(limit):
    for i in limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i, "odd")   

# showNumbers([(range(0,20)])  """ python3 doesnot return list if range is [] instead use list"""
showNumbers(list(range(0,20)))            

#10 Write a program which can filter() to make a list whose elements are even
#  number between 1 and 20 ( both included)

def filter(arg):
    l1=[]
    for i in arg:
        if i%2==0:
            l1.append(i)
    print(l1)       
filter(list(range(0,20)))     








