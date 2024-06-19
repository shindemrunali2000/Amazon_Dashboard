#..............................Set......................
# sets is a collection of non repetetive elements (repetetive element not allowed)
# set are unordered 
# set are unindexed
# There is no way to change items in sets
# sets cannot contain deblicate value
s= {1,2,3,4,1}
print(type(s))      # output <class 'set'>
print(s)            # output {1,2,3,4}


# Empty set
# Important: This Syntax will Create an empty dictionary and not an empty set
s1={}
print(type(s1))      #output <class 'dict'>


# Important: An empty set can be created using the below syntax
s2=set()
print(type(s2))
s2.add(4)
s2.add(10)
print(s2)    # output {10,4}

# unhasheble type: list 
#s3 = { 1,2 ,3,[4,5]}
#print(s3)     # output error

# hasheble type : tuple
s4 = {1,2,3,(4,5)}
print(s4)     # output {3, 1, (4, 5), 2}


# unhasheble type : dict
#s5 ={1,2,3,{4:5,6:7}}
#print(s5)    # output error

# prints the length of the set
s6 ={1,2,5,3,(4,5)}
print(len(s6))     # output 4



# remove Method
s7 ={1,2,5,3,(4,5)}
s7.remove(5)
print(s7)           # output {1,2,3,(4,5)}


# Add method
s8 ={1,2,5,3,(4,5)}
s8.add(6)
print(s8)           # output {1,2,3,(4,5),5,6}


# pop method
s9 ={1,2,5,3,(4,5)}
print(s9.pop())           # output 1  (Randam kahi pan remove karat )


# clear method
s10 ={1,2,5,3,(4,5)}
print(s10.clear())   # output none

# union method
s11 ={1,2,5,3,(4,5)}
print(s11.union({7,8}))  # output  {1, 2, 3, (4, 5), 5, 7, 8}



#intersection method
s12 ={1,2,5,3,4,5,(4,5,7)}
print(
    s12.intersection({4,5})) #output {4, 5}
