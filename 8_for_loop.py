'''Write a program to print 10 times "hello world".'''
# for i in range(1, 11):
#     print(f"Hello World")


'''Write a program to use for loop in range start, stop, step'''
# for i in range(1, 17, 5): #(1-Start, 17-Stop, 5-Step)
#     print(i)


'''Write a program to use for loop in reverse range start, stop, step'''
# for i in range(10, 0, -1):
#     print(f" Hello World {i}")


'''Make a code to take input of a number and print the sum of numbers till it'''
# num = int(input("Enter any Number: "))
# add = 0
# for i in range(1, num + 1): 
#     add = add + i 
# print(f"The sum is: {add}")


'''Make a code to take input of a number and prints its multiplication table'''
# num = int(input('Enter any number : '))
# for i in range (1, 11):
#     print(f'{num} x {i} = {num * i}')


'''Make a code to take input of a number and print even or odd numbers till it'''
# num = int(input("Enter any Number: "))
# for i in range(1, num + 1): 
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


'''Write a program to calculate the factorial of a number'''
# num = int(input("Enter any Number: "))
# fact = 1
# i = 1
# for i in range(1, num + 1): 
#     fact = fact * i
# print(f"The Factorial is: {fact}")


'''Make a code to take input of a number and calculate the sum of all even and odd numbers till it.'''
# num = int(input("Enter any Number: "))
# evensum = 0
# oddsum = 0
# for i in range(1, num + 1): 
#     if i % 2 == 0:
#         evensum = evensum + i
#     else:
#         oddsum = oddsum + i
# print(f"The sum of all even numbers is: {evensum}")
# print(f"The sum of all odd numbers is: {oddsum}")


'''Make a code to take input of a number and print the cube of all numbers till it'''
# num = int(input("Enter any Number: "))
# for i in range(1, num + 1):
#     print(f"The cube of {i} is: {i * i * i}")


'''Write a Python Program to Print the Fibonacci sequence.'''
# # 0 1 1 2 3 5 8 13
# #   a       b       c
# #   -1      1       0         c = a + b
# #   1       0       1         a = b
# #   0       1       1         b = c    
# #   1       1       2
# #   1       2       3
# #   2       3       5
# num = int(input("Enter any Number: "))
# a = -1
# b = 1
# c = 0
# for i in range(1, num + 1):
#     c = a + b
#     print(c)
#     a = b
#     b = c


'''Make a code to take input of a number and check its prime or composite'''
# num = int(input("Enter any Number: "))
# flag = False
# for i in range(2, num):
#     if num % i == 0:
#         flag = True
#         break
# if flag == True:
#     print(f"{num} is Composite")
# else:
#     print(f"{num} is prime")

