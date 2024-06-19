#...................................List.........................
#create a list using []
# a=[1 ,2,3,4,5,6,7]
# print(a[0])  # output 1
# print(a[-1]) # output 7

# change the value of list using 
# a[0]= 10
# a[1]=11
# print(a)   # output [10,11,3,4,5,6,7]



# we can create a list with items of differnt types
# b=['mrunali',10,10.5,True]
# print(b)    # output ['mrunali',10,10.5,True]


# list slicing
# friends=['tejashree','Amruta','ruchita','Asmita','radha']
# print(friends[0:4])    # output ['tejashree', 'Amruta', 'ruchita', 'Asmita']
# print(friends[-4:])    # output ['Amruta', 'ruchita', 'Asmita', 'radha']
# print(friends[1:])     # output ['Amruta', 'ruchita', 'Asmita', 'radha']
# print(friends[:4])     # output ['tejashree', 'Amruta', 'ruchita', 'Asmita']



# list Method
# 1) Sort Method
# l1 = [6,8,2,4,10,14,18,16,20,12]
# l1.sort()
# print(l1)      # output [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2) reverse method
# l2 =[3,4,2,1,7,9,10,20]
# l2.reverse()
# print(l2)     # output [20, 10, 9, 7, 1, 2, 4, 3]


# 3) append method
# l3 =['mrunal',10,True,10.8]
# l3.append(2000)
# print(l3)       # output ['mrunal', 10, True, 10.8, 2000]


# 4) insert method 
# l4 =[4,5,6,7,8,9]
# l4.insert(0,3)
# print(l4)     # output [3, 4, 5, 6, 7, 8, 9]


# 5) pop method
# l5 =[1,2,3,8,4,5,6,7]
# l5.pop(3)
# print(l5)   #output [1, 2, 3, 4, 5, 6, 7]

# 6) remove method 
# l6 = [1,2,3,8,4,5,6,7]
# l6.remove(8)
# print(l6)  # output [1, 2, 3, 4, 5, 6, 7]


# 7) extend method
# 8) clear method
# 9) index method
# 10) count method
# 11) copy method
# 12) any method
# 13) all method
# 14) ascii method
# 15) bool method
# 16) filter method
# 17) len method
# 18) max method
# 19) min method
# 20) sum method






# Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)



# Concatenate two lists index-wise             
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=zip(list1,list2)
# list4=[]
# for a ,b in list3:
#     print(a+b)
#     list4.append(a+b)
# print(list4)





#  Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# numbers = [1, 2, 3, 4, 5, 6, 7]
# square1=[]
# for i in numbers:
#     square1.append(i*i)
# print(square1)




# Concatenate two lists in the following order     
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = []
# for i in list1:
#     for j in list2:
#         list3.append(i+j)
#         # print(i + j)
# print(list3)

# Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# x=zip(list1,list2)
# for a,b in x:
#     print(a,b)


# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1=list(filter(None,list1))
# print(list1)



# Add new item to list after a specified item                      
# Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
# list1[2][2].append(7000)
# print(list1)




# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3]=200
# print(list1)



#  Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in list1:
#     if i==20:
#         list1.remove(20)
# print(list1)





# Given a list, write a Python program to swap first and last element of the list.
# List=[12, 35, 9, 56, 24]
# List[-1],List[0]=List[0],List[-1]
# print(List)



# Python program to swap two elements in a list
# List = [23, 65, 19, 90]
# List[0],List[2]=List[2],List[0]
# print(List)



# Python | Ways to find length of list
# lst = [10,20,30,40]
# print(len(lst))



# Maximum of two numbers in Python
# a = 2 
# b = 4
# if a>b:
#     print("a is Max")
# else:
#     print("b is Max")

# Python | Ways to check if element exists in list
# test_list = [1, 6, 3, 5, 3, 4]
# if 3 in test_list:
#     print("True")
# else:
#     print("False")


# Different ways to clear a list in Python
# List=[2, 3, 5, 6, 7]
# List.clear()
# print(List)



# Python | Reversing a List
# list = [4, 5, 6, 7, 8, 9]
# list.reverse()
# print(list)



# Python | Cloning or Copying a list
# list = [4, 5, 6, 7, 8, 9]
# list.copy()
# print(list)


# Find sum and average of List in Python
# List=[4, 5, 1, 2, 9, 7, 10, 8]
# a=0
# for i in List:
#     a=a+i
# print(a)
# for j in List:
#     b=a/len(List)  
# print(b) 
   
    

# Python | Multiply all numbers in the list
# list1 = [1, 2, 3]
# a=1
# for i in list1:
#     a=a*i
# print(a)



# Python program to find smallest number in a list
# list1 = [10, 20, 4]
# for i in list1:
#     list1.sort()
# print(list1[0])



# Python program to find largest number in a list
# list1 = [10, 20, 4]
# a=float('inf')
# for i in list1:
#     if i<=a:
#        a=i
# print(a)


# Python program to find second largest number in a list
# list1 = [10, 20, 4]
# for i in list1:
#     list1.sort()
# print(list1[-2])


# Python program to count Even and Odd numbers in a List
# list1 = [2, 7, 5, 64, 14]
# a=0
# b=0
# for i in list1:
#     if i%2==0:
#         a=a+1
# print(a)
# for j in list1:
#     if not j%2==0:
#         b=b+1
# print(b)




# Python program to count positive and negative numbers in a list
# list1 = [2, -7, 5, -64, -14]
# a=0
# b=0
# for i in list1:
#     if i<0:
#         a=a+1
# print("Total negetive number in list is :"+str(a))
# for j in list1:
#     if j>0:
#         b=b+1
# print("Total negetive number in list is :"+str(b))




# Python | Convert a List into a Tuple
# List=[1, 2, 3, 4]
# print(tuple(List))





# Python Program to Convert a List to String
# List=['Geeks', 'for', 'Geeks']
# str1=" ".join(List)
# print(str1)
    


# Merge Two Lists in Python
# test_list1 = [1, 4, 5, 6, 5]
# test_list2 = [3, 5, 7, 2, 5]
# test_list3=test_list1+test_list2
# test_list3.sort()
# print(test_list3)




# Python Program to Check if a String is Palindrome or Not
a="malayalam"
if a==a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

