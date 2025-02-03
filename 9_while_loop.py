'''Write a program to 'hello world' 10 times to use of while loop'''
# i = 1
# while i <= 10:
#     print(f"Hello World {i}")
#     i += 1


'''Write a program to take input of a number and check even and odd numbers till it'''
# num = int(input("Enter any Number: "))
# i = 1
# while i <= num: 
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#     i += 1 


'''Write a program to print multiplication table of a number'''
# num = int(input("Enter any Number: "))
# i = 1
# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i += 1


'''Make a code to take input of a number and calculate the sum of all even and odd numbers till it.'''
# num = int(input("Enter any Number: "))
# evensum = 0
# oddsum = 0
# i = 1
# while i <= num: 
#     if i % 2 == 0:
#         evensum = evensum + i 
#     else:
#         oddsum = oddsum + i 
#     i += 1 
# print(f"The sum of all even numbers is: {evensum}")
# print(f"The sum of all odd numbers is: {oddsum}")


'''Write a program to print take input till the user wants and print how many positive negative and zeros user entered'''
# num = None
# pcount = 0
# ncount = 0
# zcount = 0
# while True:
#     num = int(input("Enter any Number: "))
#     if num > 0:
#         pcount += 1
#     elif num == 0:
#         zcount += 1
#     else:
#         ncount += 1
#     choice = input("Do you want to continue: ")
#     if choice == 'No':
#         break
# print(f"The number of Postive Digits are: {pcount}")
# print(f"The number of Negative Digits are: {ncount}")
# print(f"The number of Zeros are: {zcount}")


'''Write a program to calculate the factorial of a number'''
# num = int(input("Enter any Number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact * i
#     i += 1
# print(f"The Factorial is: {fact}")


'''Write a progam to take input from user any digits of number and check how many digits in number'''
# num = int(input("Enter any Number: "))
# count = 0
# while num != 0: 
#     num = num // 10
#     count += 1 
# print(f"The number of Digits are: {count}")


'''Write a program to take input number from user and print to reverse form'''
# num = int(input("Enter any Number: "))
# rem = 0
# result = 0
# while num != 0: 
#     rem = num % 10
#     result = result * 10 + rem 
#     num = num // 10
# print(f"The reversed number is: {result}")


'''write a program to take input number from user and check it is palindrome number or not.'''
# num = int(input("Enter any Number: "))
# rem = 0
# result = 0
# q = num
# while q != 0:
#     rem = q % 10
#     result = result * 10 + rem
#     q = q // 10
# if result == num:
#     print(f'{num} is Palindrome number.')
# else:
#     print(f'{num} is not Palindrome number.')
