''' A Dictionary in Python is a built-in data structure that allows you to store data in key-value pairs. It is mutable, unordered (prior to Python 3.7), and optimized for fast lookups by keys. Dictionaries are extremely useful for associating unique keys with values. '''
'======================================================================='
''' **Key Features:** ''' 
# 1. **Keys**:- Must be unique and immutable (e.g., strings, numbers, tuples).
# 2. **Values**:- Can be of any data type (strings, numbers, lists, etc.).
# 3. **Mutable**:- You can add, update, or remove key-value pairs.
'======================================================================='
'''**Creating a Dictionary**'''
'Empty dictionary :-'
# my_dict = {}

'Dictionary with values'
# person = {
#     "name": "John",
#     "age": 25,
#     "city": "New York"
# }
'======================================================================='
''' **Accessing Values** '''
# print(person["name"])  # Output: John
'======================================================================='
''' **Using `get()` to Avoid KeyErrors** '''
# print(person.get("name"))  # Output: John
# print(person.get("salary", "Not Found"))  # Output: Not Found
'======================================================================='
''' **Adding/Updating Items** '''
# person["age"] = 26  # Update value
# person["gender"] = "Male"  # Add new key-value pair
'======================================================================='
''' **Removing Items** '''
# person.pop("age")  # Removes 'age' key
# del person["city"]  # Removes 'city' key
# person.clear()  # Clears all items
'======================================================================='
''' **Looping Through a Dictionary** '''
# for key, value in person.items():
    # print(f"{key}: {value}")
'======================================================================='
''' **Common Methods**
___________________________________________________________________
|      Method      |               Description                    |
|------------------|----------------------------------------------|
| dict.keys()      | Returns a view object of all keys            |
| dict.values()    | Returns a view object of all values          |
| dict.items()     | Returns a view object of key-value pairs     |
| dict.update()    | Updates dictionary with another dictionary   |
| dict.pop(key)    | Removes the specified key                    |
| dict.clear()     | Clears all items in the dictionary           |
|_________________________________________________________________|
'''
'======================================================================='
''' **Example Usage** '''
'Merging dictionaries'
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict1.update(dict2)  # {'a': 1, 'b': 3, 'c': 4}
'''
Dictionaries are versatile and commonly used in Python for storing and managing data efficiently.
'''
'======================================================================='

'''The Prime Step'''

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com", 10: "Lara", 56: 90}
# print(type(dic1))
# print(dic1)
# print(dic1["age"])
# print(dic1[10])
# print(dic1[56])
'======================================================================='

'''dict.update()
Definition: Updates the dictionary with the key-value pairs from another dictionary or iterable.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic2 = {"Profession": "Programmer", "Contact": 5674656}
# dic1.update(dic2)
# print(dic1)

# dic1 = {"Name": "John", "age": 20}
# dic2 = {"Contact": 345678, "email": "John@test.com"}
# dic3 = dic1.copy()
# dic3.update(dic2)
# print(dic3)
'======================================================================='

'''dict.popitem()
Definition: Removes and returns the last inserted key-value pair as a tuple.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic1.popitem() #Output:- Delete last key:value
# print(dic1)
'======================================================================='

'''dict.pop(key, default)
Definition: Removes the key and returns its value; returns default if the key is not found.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic1.pop("Name") #Output:- Delete 'Name' value
# print(dic1)

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# value = dic1.pop("age", "This key does not exist")
# print(value)
'======================================================================='

'''dict.clear()
Definition: Removes all items from the dictionary.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic1.clear() #Output:- Blank Dictionary
# print(dic1)
'======================================================================='

'''dict.get(key, default)
Definition: Returns the value for the specified key; returns the default value if the key is not found.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# print(dic1["age"])
# print(dic1.get("age"))
'======================================================================='

'''dict.copy()
Definition: Returns a shallow copy of the dictionary.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic3 = dic1.copy()
# print(dic3)
'======================================================================='

'''dict.fromkeys(iterable, value=None)
Definition: Creates a new dictionary with keys from the iterable and values set to the specified value (default is None).'''
# li = [1, 2, 3]
# dic3 = dict().fromkeys(li, "None")
# print(dic3)
'======================================================================='

'''dict.setdefault(key, default=None)
Definition: Returns the value of the specified key. If the key doesn’t exist, inserts the key with the specified default value.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic1.setdefault("a", 12)
# print(dic1)
'======================================================================='

'''dict.keys()
Definition: Returns a view object with all the keys in the dictionary.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# print(dic1.keys())

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# for key in dic1.keys():
#     print(f"The value on {key} is: {dic1[key]}")
'======================================================================='

'''dict.values()
Definition: Returns a view object with all the values in the dictionary.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# print(dic1.values())

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# for value in dic1.values():
#     print(f"{value}")
'======================================================================='

'''dict.items()
Definition: Returns a view object with all key-value pairs as tuples.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# print(dic1.items())

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# for key, value in dic1.items():
#     print(f"The value on {key} is: {value}")
'======================================================================='

'''del dict[key]
Removes the key-value pair associated with the specified key.'''
# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# del dic1
# print(dic1) #Output:- Not defined dic1
'======================================================================='

''' questions:-'''

'''1. Write a Python script to add a key to a dictionary.'''
'''1. Make a program to take add a key in dictionary.'''
# dic = {"Name": "John", "Age": 34}
# key = input("Enter the key: ")
# value = input("Enter the value: ")
# dic.update({key: value})
# print(dic)


'''2. Write a Python script to check whether a given key already exists in a dictionary.'''
'''2. Make a program to take input of a key and check if the key exists in the dictionary.'''
# dic = {"Name": "John", "age": 30, "email": "John@test.com"}
# key = input("Enter the key: ")
# flag = False
# for i in dic:
#     if i == key:
#         flag = True
#         print(f"{key} is in the dictionary")
#         break
# if not flag:
#     print(f"{key} is not in the dictionary")


# dic = {"Name": "John", "age": 30, "email": "John@test.com"}
# key = input("Enter the key: ")
# if key in dic:
#     print(f"{key} is in the dictionary")
# else:
#     print(f"{key} is not in the dictionary")


'''3. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).'''
# num = int(input("Enter any Number: "))
# dic = {}
# for i in range(1, num + 1):
#     dic.update({i: i * i})
# print(dic)


'''4. Write a Python script to check whether a given key already exists in a dictionary then remove and print new script.'''
# dic = {"Name": "John", "Age": 30, "Contact": 56436}
# key = input("Enter key: ")
# if key in dic:
#     dic.pop(key)
#     print(f"{key} was in the dictionary and is now removed. \n New dictionary after removing: \n {dic}")
# else:
#     print(f"{key} was not found in the dictionary.")


'''5. Write a Python program that takes a string as input and counts the occurrences of each character in the string. Store the counts in a dictionary where the keys are the characters, and the values are their respective counts. Finally, print the dictionary.'''
'''5. Write a Python program to create a dictionary from a string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
'''
# string = input("Enter any string : ")
# dic = {}
# for i in string:
#     count = string.count(i)
#     dic.update({i: count})
# print(dic)
'======================================================================='


# li = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(li[1][2])
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(li[i][j])
'======================================================================='

# li = [
#     {"Name": "John", "Age": 40},
#     {"Contact": 345645, "Email": "John@test.com"},
#     {"Profession": "Programmer", "Language": "Python"}
# ]
# print(li[2]["Language"])
'======================================================================='

# dic1 = {
#     "C": ["Vscode", "Clion"],
#     "Python": ["Vscode", "Pycharm"],
#     "Employee": {"Profession": "Programmer", "Languages": {"Python": ["Backend", "Data Scienece"], "Java": {"IDE": ["Eclipse", "Intelli J"]}}}
# }
# print(dic1["C"][1])
# print(dic1["Employee"]["Languages"]["Java"]["IDE"][0])
'======================================================================='

''' questions:-'''
'''
1. Write a Python program to combine two dictionary by adding values for common keys.
2. Write a Python program to drop empty items from a given dictionary.
'''