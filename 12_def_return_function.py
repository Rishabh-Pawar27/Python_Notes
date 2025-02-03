'''#) Function return '''
# def sqr(a):
#     return a * a
# x = sqr(5)
# print(x)

'''Make a code to take input of a number and check its prime or composite to use of def return function'''
# def check_prime():
#     num = int(input("Enter any Number: "))
#     flag = False
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         return True
#     else:
#         return False
# if check_prime():
#     print("Composite")
# else:
#     print("Prime")


'''write a function return program to take input number from user and check it is palindrome number or not.'''
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
#         return True
#     else:
#         return False
# if check_palindrome():
#     print("Plaindrome")
# else:
#     print("Not Palindrome")


'''Write a code of return value'''
# def fun(x):
#     n = None
#     if x == 1:
#         return x
#     else:
#         n = x + fun(x - 1)
#         return n
# num = int(input('Enter any number : '))
# var = fun(num)
# print(f'The value is: {var}')
