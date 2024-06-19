# while loop
#i=0
#while i <10:
#    print("Yes"+str(i))
#    i=i+1
#print("done")      



#i = 1
#while i<=50:
    #print(i)
#    i=i+1
    


#fruits = ['mango','greaps','Banana','watermelone']
#i=0
#while i<len(fruits):
#    print(fruits[i])
#    i=i+1



#for loop
#fruits = ['mango','greaps','Banana','watermelone']
#for item in fruits:
#    print(item)
    



# # for a in range(8):
#     print(a)   #output 0 1 2 3 4 5 6 7


# for i in range(2,8):
#     print(i)   #output 2 3 4 5 6 7

# for c in range(1,8,2):
    # print(c)  #output 1 3 5 7



# for i in range(10):  
#     print(i)
# else:               # ( loop ending zalyaver else print zala)
#     print("This is inside else of for ")   # 1  2 3 4 5 6 7 8 9  this is inside else of for


# break statement
# for i in range(10):  
#     print(i)
#     if i==5:
#         break
# else:               
#     print("This is inside else of for ")   # output 0 1  2 3 4 5 




# continue statement
# for i in range(10):  
#    if i==5:
#          continue
#    print(i)             # output 1 2 3 4  6 7 8 9  (5 skip)


#pass statement
# pass is null statement in python 
# it interests to "do nothing"
# i=4
# if i>0:
#     pass
# while i>6:
#     pass
# print("mrunal is good girl")



#reverse table
# num= int(input("Enter the number: "))
# for i in range(10,0,-1):
#     print(f"{num}*{i}={num*i}") 
    



# Print First 10 natural numbers using while loop
# for i in range(1,11):
#     print(i)


# Write a program to print the following number pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# a=0
# for j in range (1,6):
#     for i in range(1,(1+j)):
#             print(i,end=" ")
#     print("\t\t")


# Calculate the sum of all numbers from 1 to a given number
# def my_fun():
   
#     n=int(input("Enter your number"))
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)

# my_fun()



#  Write a program to print multiplication table of a given number
# def my_fun():
#     n=int(input("Enter your number"))
#     mult=1
#     for i in range(1,11):
#         mult=i*n
        
#         print(mult)

# my_fun()




# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i>500:
#             break
#     if i%5==0:
#         if i>150:
#            continue
#         print(i)              

                
                


# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# n=[]
# for i in range(1500,2700):
#     if (i%7==0 and i%5==0):
#         n.append(str(i))
# print(n)



# Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# for i in range(1,6):
#     for j in range(1,(1+i)):
#         print("*",end=" ")
#     print("\t\t")
# for x in range(1,6):
#     for k in range(1,(6-x)):
#         print("*",end=" ")
#     print("\t\t")



# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(0,7):
    # 1 2 3 4 5 6
    if i==6 or i==3:
       continue
    print(i)
        
   
    