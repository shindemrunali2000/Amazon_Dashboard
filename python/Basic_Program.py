from datetime import date
# n=input("Enter your number :")

# list=n.split(" ,")
# tuple = tuple(list)
# print("List:", list)
# print("tuple:",tuple)


# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# def my_fun(a,b):
#     Sum=a+b
#     mult=a*b
#     if mult<= 1000:
#         print("The multiplication is: " +str(mult))
#     else:
#         print("The addition is: "+str(Sum))

# a=int(input("Enter your First Number:"))
# b=int(input("Enter your Second Number :"))

# my_fun(a,b)



# Print the sum of the current number and the previous number
# prev_num=0
# for i in range(10):
#     print("Privious Number is :" +str(prev_num) + "  " + "Current number is :"+str(i) + "  " + "Addition is : "+str(prev_num+i))
#     prev_num=i




#  Print characters from a string that are present at an even index number
# str="pynative"
# for i in range(0,len(str),2):
#   print(str[i])                         //output : 



#  Remove first n characters from a string
# str1="pynative"
# print(str1[2:])                          //output : native





# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# if numbers_y[0]== numbers_y[-1]:
#     print("True")
# else:
#     print("false")               //output:false




# Display numbers divisible by 5 from a list
# list1=[10, 20, 33, 46, 55]
# for i in list1:
#     if i%5==0:
#         print(i)



# Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
# str_x = "Emma is good developer. Emma is a writer"
# print("Emma appeared " +str(str_x.count("Emma")) + " time")      //output:Emma appeared 2 time




# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
# num=124
# numstr = str(num)

# if numstr == numstr[::-1]:
#     print("Palindrome")
# else:
    # print("Not Palindrome") 



# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# newlist=[]
# for i in list1 :
#     if i%2!=0:
#          newlist.append(i)
# for j in list2:
#       if j%2==0:
#           newlist.append(j)
    
# print(newlist)



#  Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
# num=7536
# strnum=str(num)
# print(strnum[::-1])
# result = map(int, strnum)
# print(list(result))


# Calculate income tax for the given income by adhering to the rules below 45000
# Taxable Income	Rate (in %)
# First $10,000	      0
# Next $10,000	      10
# The remaining	      20

# income=45000
# if income >= 10000 and income<20000:
#     a=income-10000
#     tax=a*(10/100)
#     print(tax)

# if income>20000:
#     b=income-20000
#     tax1= 10000*(10/100) + b*(20/100)
#     print(tax1)




# Print multiplication table from 1 to 10
# a=0
# for j in range(10):
#     a=a+1
#     b=0
#     for i in range(10): 
#         b=b+a
#         print(b, end=" ")
#     print("\t\t")


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")





# Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *
# for i in range(1,6):

#     #1 ,2, 3 ,4 ,5 
#     for j in range(1,(7-i)):
#         print("*",end=" ")
        
#     print("\t\t")

# Print a upward Half-Pyramid Pattern of Star (asterisk)   
# * 
# * * 
# * * *
# * * * *
# * * * * *
# for i in range(1,6):

#     #1 ,2, 3 ,4 ,5 
#     for j in range(1,(1+i)):
#         print("*",end=" ")
        
#     print("\t\t")




# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
# def exponent(base, exp):
#     a=base**exp
#     print(str(base) + " raises to the power of " +str(exp)+ ":" +str(a))
# exponent(2,5)   
      
      

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# Fristname=input("Enter Your First Name :")
# Lastname=input("Enter your last name :")
# name=Fristname+Lastname
# print(name[::-1])


# Wri te a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# a=[]
# def my_fun(*abc):
#     for i in abc:
#         a.append(str(i))
#     print(a)
#     b=tuple(a) 
#     print(b)
# my_fun(3,5,7,23)





# a=input("Enter Your File Name :")

# b=a.split(".")
# print("The extension of the file is : " + repr(b[-1]))




# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# print(color_list[0] +" "+ (color_list[-1]))




# Write a Python program to count the number 4 in a given list.
# List=[1,2,3,4,5,4,4]
# a=List.count(4)
# print(a)


