#.................................Dictionary.....................
# dictionary is unordered
# it is mutable / it is changeble
# cannot contain dublicate keys    
# dict ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76}

# }
# print(dict['radha'])      # output  good girl
# print(dict['mayuri'])     # output  lovely girl
# print(dict['marks'])      # output  [1,2,3]
# print(dict['dictionary']) # output  {'sita': 45, 'gita': 76}
# print(dict['dictionary']['sita'])  # output 45



# dictionary methods
# 1) prints the keys of dictionary
# dict1 ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76},
#     1:2
# }
# print(dict1.keys())    # output dict_keys(['radha', 'mayuri', 'marks', 'dictionary', 1])


# 2) print the values of the dictionary
# dict2 ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76},
#     1:2
# }
# print(dict2.values())    # output  dict_values(['good girl', 'lovely girl', [1, 2, 3], {'sita': 45, 'gita': 76}, 2])

# 3) item method or print the (key , value)for all contents of the dictionary

# dict3 ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76},
#     1:2
# }
# print(dict3.items())    # output dict_items([('radha', 'good girl'), ('mayuri', 'lovely girl'), ('marks', [1, 2, 3]), ('dictionary', {'sita': 45, 'gita': 76}), (1, 2)])



# 4) updete method  / updates the dict4 by adding key values pairs form updatedict
# dict4 ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76},
#     1:2
# }
# updateDict ={
#     "Tejashree":'Friend'

# }
# dict4.update(updateDict)
# print(dict4)       # output {'radha': 'good girl', 'mayuri': 'lovely girl', 'marks': [1, 2, 3], 'dictionary': {'sita': 45, 'gita': 76}, 1: 2, 'Tejashree': 'Friend'}


# # 5) get method (interview question)
# dict5 ={
#     "radha":"good girl",
#     "mayuri":"lovely girl",
#     "marks":[1,2,3],
#     "dictionary":{'sita':45,'gita':76},
#     1:2
# }

# print(dict5.get("marks"))   # output [1,2,3]
# print(dict5["marks"])       # output [1,2,3]

# # differnces
# print(dict5.get("marks1")) # returns none as marks1 is not present in the dictionary  output none
# #print(dict5["marks1"]) # throws an error as marks1 is not present in the dictionary both output is different   output error





# Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1=zip(keys,values)
# print(dict(dict1))




# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)




# Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# abc=sampleDict["class"]["student"]["marks"].get("history")
# print(abc)




# Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# list1=[]
# for i in employees:
#     list1.append(i+str(defaults))
# print(list1)
# /////////////////////////////////////or//////////////
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# thisdict = dict.fromkeys(employees,defaults)
# print(thisdict)






# Create a dictionary by extracting the keys from a given dictionary              ++++++++++++++
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys ="name"
# list1=[]
# for i in sample_dict:
#     if i==n:
#         list1.append(keys)
# print(list1)
        

# sample_dict.remove(keys)
# print(sample_dict)
# for x in sample_dict.items():
    
#         mydict = sample_dict.copy()
# print(mydict)






# Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if sample_dict.get("",200)==None:
#     print("200 is not present in dict ")
# else:
#     print("200 is present in dict ")




# Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location'] = sample_dict['city']
# del sample_dict['city']
# print( str(sample_dict))



# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# a=min(sample_dict.keys())
# print(a)
    

# Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)


