

# Write a program to create a function that takes two arguments, name and age, and print their value.
# def my_fun(name,age):
#     print("Enter your full name is :"+name,age)
# name=input("Enter Your Name :")
# age=input("Enter Your Name :")
# my_fun(name,age)




# Write a program to create function func1() to accept a variable length of arguments and print their value.
# def my_fun(*abc):
#     for i in abc:
#         print(i)
# print("Printing Values")
# my_fun(20, 40, 60,70,80)




# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# def calculation(a, b):
#     c=a+b
#     d=a-b
#     print("additon is :" +str(c) + " substraction is :"+ str(d) )
# calculation(40,10)


# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# def show_employee(name,salary=9000):
#     print("Name : "+str(name)+ " \nsalary :"+str(salary))

# show_employee("Mrunali")



# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
# def outer(a,b):
#     def inner(x,y):
#         c= x+y
#         return c
    
#     print("Result: "+ str(inner(a,b)))
#     print("Total: ", str(inner(a,b) + 5))

# outer(10,20)

#User function output outside the function (return c)
# def export1(a,b):
#     c=a+b
#     return c
#     ## print(c)

# def abc(x,y):
#     d=x+y+export1(10,20)
#     print(d)

# abc(10,10)



# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.
# a=0
# for i in range(0,11):
#     a=a+i
# print(a)
    
# /////////////////////////////OR/////////////////////////////////  
# def addition(a,b):
#     for i in range(a,b):
#         a=a+i
#     print(a)
# addition(0,20)




# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
# def display_student(name,age):
#     print(name,age)
# show_student=display_student
# show_student("Mrunali","23")




# Generate a Python list of all the even numbers between 4 to 30
# def my_fun():
#     list1=list()
#     for i in range(4,30):
#             if i%2==0:
#                 list1.append(i)
#     print(list1)
# my_fun()



# Find the largest item from a given list
# x = [4 ,24,6, 8,  12, 2,50]
# ln=0
# c=[]
# for i in x:
#     if i>=ln:
#        ln=i
#        c.append(ln)
# print(c[-2:])


#  Write a Python function to find the maximum of three numbers.
# 10,20,30      
# def my_fun(a,b,c,f):
#     d=[a,b,c,f]
    
#     ln=0               
#     for i in d:
#         if i>=ln:
#             ln=i
#     print(ln)
# my_fun(50,20,30,40)

# //////////////////////////////////or////////////////////

# def my_fun(*abc):
#     d=[*abc]
#     ln=0 
#     for i in d:
#        if i>=ln:
#             ln=i
#     print(ln)
# print("Printing Values")
# d=input("a :")
# my_fun(20, 40, 60,70,80)
    
 

# Write a Python function to sum all the numbers in a list.
# a=[8, 2, 3, 0, 7]
# b=0
# for i in a:
#     b=b+i
# print(b)




# Write a Python function to multiply all the numbers in a list.
# a=[8, 2, 3, -1, 7]
# b=1
# for i in a:
#      b=b*i
# print(b)




# Write a Python program to reverse a string. 
# def my_fun(Str):
#     return Str[::-1]
# a=my_fun("1234abcd")
# print(a)



# Write a Python function to check whether a number falls within a given range.
# def my_fun(n):
#     if n in range(1,10):
#         print("Number is present in range")
#     else:
#         print("Number is not present in range")
        
# my_fun(11)



#  Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'

# def my_fun(x):
#     count1=0
#     count2=0
#     count3=0
#     newstring=''
#     for i in x:
#         if (i.isupper())==True:
#             count1=count1+1
#             newstring+=(i.lower())
#         elif (i.islower())==True:
#             count2=count2+1
#             newstring+=(i.upper())
#         else:
#             (i.isspace())==True
#             count3=count3+1
#             newstring+=i
#     print(newstring)
#     print(count1)
#     print(count2)
#     print(count3)



# my_fun('The quick Brow Fox')




#  Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def my_fun(abc):
#     b=[]
#     for i in abc:
#         if not i in b:
#             b.append(i)
#     print(b)
# a=[1,2,3,3,3,3,4,5]
# my_fun(a)



# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def my_fun(abc):
#     for i in abc:
#         if i%2==0:
#             print(i)
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# my_fun(a)




# Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# def my_fun(a):
#     if a==a[::-1]:
#         print("pallindrome")
#     else:
#         print("not pallindrome")
#     print(a)
# my_fun("The quick brown fox jumps over the lazy dog")




# Write a Python function to check whether a number is "Perfect" or not.
# 6 la 1 2 3 and 6 he sagale 6 che divisor ahete tyat 6 sodun 1+2+3 yachi addition karun 6 ale ter num is perfect
# def my_fun(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
#     return sum==n
# print(my_fun(6))



# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
# def my_fun(x):
#     a=[]
#     for i in range(1,x):
#         a.append(i*i)    
#     print(a)
# my_fun(30)


# Write a Python program to access a function inside a function.
# def my_fun(a,b):
#     c=a+b
#     return c
# def my_fun1():
#     d=my_fun(2,3)*2
#     print(d)

# my_fun1()



# Write a Python program to detect the number of local variables declared in a function.
local1=4
def my_fun():
    global1=3
    print(local1)
    print(global1)
my_fun()


