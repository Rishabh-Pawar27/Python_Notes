'''def function_name(parameter1, parameter2)'''

'''Write a program to two numbers addition use of  def function.'''
# def add(a, b):
#     print(f"The Addition is: {a + b}")
# add(20, 50)
# add(89, 12)
# add(90, 45)
# add(78, 23)


'''write a program input no. of user and print its multiplication table use of def function'''
# def table():
#     num = int(input("Enter any Number: "))
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num * i}")
#     print("=========================")
# table()
# table()
# table()


# num = int(input("Enter any Number: "))
# table(num)
# table(5)
# table(89)
# table(12)


'''Make a code to take input of a number and check its prime or composite to use of def function'''
# def check_prime():
#     num = int(input("Enter any Number: "))
#     flag = False
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{num} is Composite")
#     else:
#         print(f"{num} is Prime")
# check_prime()


'''write a program to take input number from user and check it is palindrome number or not.'''
# def check_palindrome():
#     num = int(input("Enter any Number: "))
#     rem = 0
#     result = 0
#     q = num
#     while q != 0:
#         rem = q % 10
#         result = result * 10 + rem
#         q = q // 10
#     if result == num:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# check_palindrome()


'''write a program to check 1 to 500 palindrome number.'''
# def check_palindrome():
#     for i in range(1, 501):
#         rem = 0
#         result = 0
#         q = i
#         while q != 0:
#             rem = q % 10
#             result = result * 10 + rem
#             q = q // 10
#         if result == i:
#             print(f"{i} is Palindrome")
#         else:
#             print(f"{i} is not Palindrome")
# check_palindrome()


'''Write a code to take input of a number and check how many digits in their'''
# def fun():
#     num = int(input("Enter any Number: "))
#     count = 0
#     while num != 0:
#         num = num // 10
#         count += 1
#     print(f"The number of Digits are: {count}")
# fun()


'''Make a code to take input of a number and calculate the sum of all even and odd numbers till it.'''
# def even_odd():
#     num = int(input("Enter any Number: "))
#     evensum = 0
#     oddsum = 0
#     for i in range(1, num + 1):
#         if i % 2 == 0:
#             evensum = evensum + i
#         else:
#             oddsum = oddsum + i
#     print(f"The sum of all even numbers is: {evensum}")
#     print(f"The sum of all odd numbers is: {oddsum}")
# even_odd()

# x = 'awesome'
# def myfunc():
# #   global x
#   x = 'fantastic'
# myfunc()
# print('Python is ' + x)