''' LIST :-
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .'''

'''List functions'''

'''APPEND - The append() method adds an item to the end of the list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.append(100) #list ke aakhri m element add ho jayega.
# print(li)

'''INSERT - The insert() method inserts an element to the list at the specified index.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.insert(2, 80)
# print(li)

'''EXTEND - The extend() method adds all the items of the specified iterable, such as list, tuple, dictionary, or string , to the end of a list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.extend([10, 20, 30])
# print(li)

'''POP - The list pop() method removes the item at the specified index. The method also returns the removed item.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.pop(1)
# print(li)

'''REMOVE - The remove() method removes the first matching element (which is passed as an argument) from the list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.remove(7.8)
# print(li)

'''CLEAR - The clear() method removes all items from the list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.clear()
# print(li)

'''COUNT - The count() method returns the number of times the specified element appears in the list.'''
# li = [45, "Hello", 90, 7.8, True, 'Hello']
# print(li)
# print(f' Hello no. of {li.count("Hello")} times in list.')

'''INDEX - The index() method returns the index of the specified element in the list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# a = li.index(True)
# print('Position of "True" in list is', a)

'''COPY - The copy() method returns a shallow copy of the list.'''
# list_1 = [45, "Hello", 90, 7.8, True]
# print('List 1 = ', list_1)
# list_2 = list_1.copy()
# print('List 2 = ', list_2)

'''REVERSE - The reverse() method reverses the elements of the list.'''
# li = [45, "Hello", 90, 7.8, True]
# print(li)
# li.reverse()
# print(li)

'''SORT - The list's sort() method sorts the list in ascending order.'''
# li = [6, 9, 23, 67, 4, 1]
# print(li)
# li.sort()
# print(li)

# li = [6, 9, 23, 67, 4, 1]
# print(sorted(li))
# print(li)


'''ASCII Value :- The full form of ASCII is American Standard Code for Information Interchange.'''
'''Digits ASCII Value :- 0-48, 1-49, 2-50, 3-51, 4-52, 5-53, 6-54, 7-55, 8-56, 9-57'''
'''Capital Letters ASCII Value :- A=65, B=66, C=67,D=68, E=69, F=70, G=71, H=72, I=73, J=74, K=75, L=76, M=77, N=78, O=79, P=80, Q=81, R=82, S=83, T=84, U=85, V=86, W=87, X=88, Y=89, Z=90'''
'''Small Letters ASCII Value :- a=97, b=98, c=99, d=100, e=101, f=102, g=103, h=104, i=105, j=106, k=107, l=108, m=109, n=110, o=111, p=112, q=113, r=114, s=115, t=116, u=117, v=118, w=119, x=120, y=121, z=122'''

'''Always list sort by ASCII value'''
# li = ['email', 'john', 'a', 'A', '9', 'Hello']
# li.sort()
# print(li)

# li = [12, 6, 89, 4, 90, "Hello", 9.8, True, 20, "John"]
# start:stop:step
# print(li[::])
# print(li[2:])
# print(li[:8])
# print(li[3:9])
# print(li[2:9:2])

# li = [12, 6, 89, 4, 90, "Hello", 9.8, True, 20, "John"]
# print(li[2])
# print(li[-8])
# print(li[len(li) - 8])
# print(li[-7:])
# print(li[2:-2])
# print(li[-1:-6:-1])
# print(li[::-1])


# li = [45, "Hello", 90, 7.8, True]
# print(type(li))
# print(li)
# print(li[2]) #print(list[element index number])

# for i in li:
    # print(i)

# for i in range(0, 5):
#     print(li[i])


'''Make a code to print list length and print all element in list.'''
# li = [56, 4, 7, 4, 7,356 ,784,567,894,345,678,567,895,453,456,7890,6545,34,67896]
# print(f'The length of list is {len(li)}')
# for i in range(0, len(li)):
#     print(li[i])


'''Make a code to sum of all integers in given list.'''
# li = [34,67,34,87,2,7,3456,58,3,6,24,58,3,70943,4567,834]
# add = 0
# for i in li:
#     add = add + i
# print(f"The sum of all elements of list is: {add}")


'''Make a code to check the even and odd number in the list.'''
# li = [5, 34, 8, 34, 8, 342, 89,356 , 98,54354,5, 3647,8,434,567,843,245]
# for i in li:
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


'''Make a code to check the minimum and maximum number in the list.'''
li = [56, 4, 87, 45, 7, 234, 876, 34, 7, 9, 234, 87]
Min = li[0]
Max = li[0]
for i in range(1, len(li)):
    if li[i] < Min:
        Min = li[i]
    if li[i] > Max:
        Max = li[i]
print(f"The minimum number in list is: {Min}")
print(f"The Maximum number in list is: {Max}")


'''Make a code to take input from user and check the number in the list or not.'''
# li = [5, 34, 78, 4, 89, 34, 7, 32, 89, 34, 67]
# num = int(input("Enter any Number: "))
# if num in li:
#     print(f"{num} is in the list")
# else:
#     print(f"{num} is not in the list")


'''Make a code to take input from user and find the number in the list if present count how many times it was repeated '''
# li = [5, 3, 7, 54, 3, 76, 98, 34, 89, 3, 342, 67, 89, 3, 132, 67]
# count = 0
# flag = False
# num = int(input("Enter any Number: "))
# for i in li:
#     if num == i:
#         flag = True
#         count += 1
# if flag:
#     print(f"{num} is in the list and was repeated {count} times")
# else:
#     print(f"{num} is not in the list")


'''Make a code to check the prime & composite number of list.'''
# li = [54, 7, 3, 89, 34, 78, 23, 9, 54, 5, 7, 17, 90, 67]
# num = int(input("Enter any Number: "))
# flag = False
# if num in li:
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{num} is in the list and is Composite")
#     else:
#         print(f"{num} is in the list and is Prime")
# else:
#     print(f"{num} is not in the list")


'''Make a code to check consecutive number in list'''
# li = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# count = 0
# maxcount = 0
# for i in li:
#     if i == 0:
#         count += 1
#         if count > maxcount:
#             maxcount = count
#     else:
#         count = 0
# print(f"The maximum number of Consecutive 1s is: {maxcount}")


'''Make a code to find Minimum, Maximum, Second_Smallest and Second_largest element in list.'''
# li = [3, 56, 30, 67, 54, 8, 90, 9, 34, 7, 32, 78]
# Min = li[0]
# Max = li[0]
# for i in range(1, len(li)):
#     if li[i] < Min:
#         Min = li[i]
#     if li[i] > Max:
#         Max = li[i]
# secsmallest = Max
# seclargest = 0
# for i in li:
#     if i != Min:
#         if i < secsmallest:
#             secsmallest = i
#     if i != Max:
#         if i > seclargest:
#             seclargest = i
# print(f"The Minimum number in array is: {Min}")
# print(f"The Maximum number in array is: {Max}")
# print(f"The Second Smallest number in array is: {secsmallest}")
# print(f"The Second Largest number in array is: {seclargest}")


'''Make a code to check input number in list and create their multiplication table.'''
# li = [34, 67, 32, 8, 32, 8, 45, 32, 8, 32, 6]
# num = int(input("Enter any Number: "))
# if num in li:
#     print(f"{num} is in the list and here is the table")
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num * i}")
# else:
#     print(f"{num} is not in the list")


'''Make to check input number in the list and check also palindrome number.'''
# li = [4, 7, 3, 8, 4, 23, 87, 54, 342, 87, 32, 1221, 45, 343]
# num = int(input("Enter any Number: "))
# if num in li:
#     rem = 0
#     result = 0
#     q = num
#     while q != 0:
#         rem = q % 10
#         result = result * 10 + rem
#         q = q // 10
#     if result == num:
#         print(f"{num} is in the list and is Palindrome")
#     else:
#         print(f"{num} is in the list and is not Palindrome")
# else:
#     print(f"{num} is not in the list")


'''Make a code to sorted list without use any function'''
# li = [56, 34, 8, 4, 2, 8, 45, 234, 890, 32]
# n = len(li)
# for i in range(0, n - 1):
#     for j in range(0, n - i - 1):
#         if li[j] > li[j + 1]:
#             temp = li[j]
#             li[j] = li[j + 1]
#             li[j + 1] = temp
# print("Sorted List")
# print(li)


'''Make a code to check even number in a list range'''
# li = [i for i in range(1, 17) if i % 2 == 0]
# print(li)

'''Make a code to check even number in a list'''
# li2 = [4, 6, 34, 7, 3]
# li3 = [i for i in li2 if i % 2 == 0]
# print(li3)


'''Make a code to print all the prime and composite numbers of list'''
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# flag = False
# for i in li:
#     flag = False
#     for j in range(2, i):
#         if i % j == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{i} is Composite")
#     else:
#         print(f"{i} is Prime")


'''Make a code to print all the prime and composite numbers of list'''
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(0, len(li)):
#     flag = False
#     for j in range(2, i):
#         if li[i] % j == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{li[i]} is Composite")
#     else:
#         print(f"{li[i]} is Prime")

'''Question:-
Write a program to make a list of 0s and 1s and find the maximum number of Consecutive 1s in it.''' "I think this question, answer given above side"