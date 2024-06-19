#..............................tuple..................
# creating a tuple using ()
# tuple are does not change it fixed element
# t=() empty tuple   # output ()
# t =(1,) single element tuple  output (1,)
t=(1,2,3,4)
print(t)    # output (1, 2, 3, 4)

# printing the element of a tuple
t1 = (1,2,3,4,5)
print(t[0])    # output 1


# cannot upadate the value of tuple
t2 = ('mrunali','nikhil','kirti','varsha')
#t2[0]='kiran'   # output error


# Tuple method
# 1) count method
t3 =(1,2,2,3,4,2,6,7) 
print(t3.count(2))     # output 3    (three time 2 repeted)


# 2) index method
t4 = (1,2,3,4,5,6,7,7,8,10)
print(t4.index(10))  # output 9 (10 element index 9)




