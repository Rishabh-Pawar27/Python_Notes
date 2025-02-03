# tup = (1, 2, 3, 4, 5)
# print(type(tup))

# tup = (1, )
# print(type(tup))

# li = [34, 5, 32, 7]
# li[0] = 1
# print(li)

# tup = (1, 2, 3, 4, 5)
# tup[0] = 10
# print(tup) #Error

# tup = (1, 2, 3, 4, 5)
# print(tup)
# for i in tup:
#     print(i)

# tup = (56, 89, 52, 87, 96)
# for i in range(0, 3):
#     print(tup[i])

# tup = (56, 89, 52, 87, 96)
# for i in range(0, len(tup)):
#     print(tup[i])


'''Tuple convert to list'''
# tup = (12, 56, 3, "Hello", 56, 6.4, True)
# temp = list(tup)
# print(temp)
# print(type(temp))

'''List convert to tuple'''
# tup = [12, 56, 3, "Hello", 56, 6.4, True]
# temp = tuple(tup)
# print(temp)
# print(type(temp))

'''Add more item end in list'''
# tup = (12, 56, 3, "Hello", 56, 6.4, True)
# temp = list(tup)
# temp.append("Good Morning")
# print(temp)

'''Remove item in list'''
# tup = (12, 56, 3, "Hello", 56, 6.4, True)
# temp = list(tup)
# temp.remove("Hello")
# print(temp)

'''Add more item end in list'''
# tup = (12, 56, 3, "Hello", 56, 6.4, True)
# temp = list(tup)
# temp.extend([10, 20, 30])
# print(temp)

'''Reverse print'''
# tup = (12, 56, 3, "Hello", 56, 6.4, True)
# temp = list(tup)
# temp.reverse()
# print(temp)


'''Make a code to input number and check in tuple array and get multiplication table'''
# tup = (4, 3, 76, 34, 543, 76 , 23, 56, 8, 32, 5, 3, 67)
# num = int(input("Enter any Number: "))
# if num in tup:
#     print(f"{num} is in the tuple and here is table")
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num * i}")
# else:
#     print(f"{num} is not in the tuple")


'''Make a code to input number and check in tuple array and count repeated times'''
# tup = (54, 34, 6, 34, 7, 32, 87, 34, 65)
# num = int(input("Enter any Number: "))
# count = 0
# flag = False
# for i in tup:
#     if i == num:
#         flag = True
#         count += 1
# if flag:
#     print(f"{num} is in the tuple and was repeated {count} times")
# else:
#     print(f"{num} is not in the tuple")

''' 
1. Make a tuple and append and remove an element from it
2. Write a program to take input from user and add that number in the list
3. Write a program to sort a list
4. Write a program to take input of a number and find the number in the list if that number exists remove it from the list.
'''
