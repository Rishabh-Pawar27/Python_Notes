'''Write a program to take input of two numbers and print the multiplication tables of all numbers between them'''
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("===========================")
# for i in range(num1, num2 + 1):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#     print("===========================")


'''Write a program to print all prime and composite numbers between 1-500'''
# for i in range(1, 501):
#     flag = False
#     for j in range(2, i):
#         if i % j == 0:
#             flag = True
#             break
#     if flag == True:
#         print(f"{i} is Composite")
#     else:
#         print(f"{i} is prime")


'''write a program to check 1 to 500 palindrome number.'''
# for i in range(11, 501):
#     rem = 0
#     result = 0
#     q = i

#     while q != 0:
#         rem = q % 10
#         result = result * 10 + rem
#         q = q // 10

#     if result == i:
#         print(f"{i} is Palindrome")
#     else:
#         print(f"{i} is not Palindrome")