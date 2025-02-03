'''if_else'''
# if 1 == 1:
#     print("Hello")
#     print("Good Morning") 


'''Write a program to input no. from user and check even and odd no.'''
# num = int(input("Enter any Number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num = int(input("Enter any number : "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


'''Write a program to input alphabate to check uppercase and lowercase'''
# ch = input("Enter any Character: ")
# if 'A' <= ch <= 'Z':
#     print("Uppercase")
# else:
#     print("Lowercase")


'''Write a program to input alphabate to check vowel or consonant'''
# ch = input("Enter any Character: ")
# if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' :
#     print("Vowel")
# else:
#     print("Consonent")


'''Write a program to input any character to check vowel or consonant or digit or special character'''
# ch = input("Enter any Character: ")
# if 'A' <= ch <= 'Z':
#     print("Uppercase Letter")
# elif 'a' <= ch <= 'z':
#     print("Lowercase Letter")
# elif '0' <= ch <= '9':
#     print("Digit")
# else:
#     print("Special Character")


'''Write a program that asks the user to input their age and gender. If the person is female and their age is between 18 and 25, display "You are eligible for the women's scholarship." For males, display "You are not eligible for the women's scholarship." For other age ranges, display "You are not eligible for any scholarships." '''
# age = int(input("Enter Your age: "))
# gender = input("Enter Your Gender: ")
# if gender == 'Female' and 18 <= age <= 25:
#     print("You are eligible for Women's Scholarship")
# elif gender == 'Male':
#     print("You are not eligible for women's scholarship")
# else:
#     print("You are not eligible for any scholarship")


'''Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.Calculate percentage and grade according to following: 
Percentage >= 90% : Grade A, 
Percentage >= 80% : Grade B, 
Percentage >= 70% : Grade C, 
Percentage >= 60% : Grade D, 
Percentage >= 40% : Grade E, 
Percentage  < 40% : Grade F. '''
# Physics = int(input("Enter the marks for Physics: "))
# Chemistry = int(input("Enter the marks for Chemistry: "))
# Biology = int(input("Enter the marks for Biology: "))
# Computer = int(input("Enter the marks for Computer: "))
# Math = int(input("Enter the marks for Math: "))
# per = (Physics + Chemistry + Biology + Computer + Math) // 5
# if 90 <= per <= 100:
#     print("Grade A")
# elif 80 <= per < 90:
#     print("Grade B")
# elif 70 <= per < 80:
#     print("Grade C")
# elif 60 <= per < 70:
#     print("Grade D")
# elif 40 <= per < 60:
#     print("Grade E")
# else:
#     print("Grade f")
# print(f"Your percentage is: {per}")


'''Make a code to take input of a number and check if it is negative or positive.'''
# num = int(input("Enter any number: "))
# if num > 0:
#     print(f'{num} is positive number')
# elif num < 0:
#     print(f'{num} is negative number')
# else:
#     print('You enter zero number')


'''Make a code to take input of a number and check if it is divisible by 5'''
# num = int(input("Enter any Number: "))
# if num % 5 == 0:
#     print("This number is divisible by 5")
# else:
#     print("This number is not divisible by 5")


'''Write a program, which will require the user to give values of hardness,  carbon  content  and  tensile  strength  of  the  steel  under consideration and output the grade of the steel. A  certain  grade  of  steel  is  graded  according  to  the  following  conditions:-  
(i) Hardness must be greater than 50 
(ii) Carbon content must be less than 0.7 
(iii) Tensile strength must be greater than 5600  
The grades are as follows:-
Grade is 10 if all three conditions are met 
Grade is 9 if conditions (i) and (ii) are met 
Grade is 8 if conditions (ii) and (iii) are met 
Grade is 7 if conditions (i) and (iii) are met 
Grade is 6 if only one condition is met 
Grade is 5 if none of the conditions are met. ''' 
# Hardness = int(input("Enter Hardness : "))
# Carbon = float(input("Enter Carbon Content : "))
# Tensile = int(input("Enter Tensile Strength : "))
# if Hardness > 50 and Carbon < 0.7 and Tensile >= 5600 :
#     print("Grade is 10")
# elif Hardness > 50 and Carbon < 0.7 :
#     print("Grade is 9")
# elif Carbon < 0.7 and Tensile > 5600 :
#     print("Grade is 8")
# elif Hardness > 50 and Tensile > 5600 :
#     print("Grade is 7")
# elif Hardness > 50 or Carbon < 0.7 or Tensile > 5600 :
#     print("Grade is 6")
# else : 
#     print("Grade is 5")


'''A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10 days fine is 1 ruppee and above 10 days fine is 5 ruppees. If return the book after 30 days your membership will be cancelled. Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message.'''
# Days = int(input("Enter no. of late days : "))
# if Days <= 5 :
# 	print(f"Fine is {Days * 0.5}")
# elif 6 <= Days <= 10 :
# 	print(f"Fine is {Days * 1.0}")
# elif 10 <= Days <= 30 :
# 	print(f"Fine is {Days * 5.0}")
# else :
#     print("Your membership will be cancelled")


'''If the three sides of a triangle are entered through the keyboard,  write  a  program  to  check  whether  the  triangle  is isosceles, equilateral, scalene.
(Isosceles Triangle is two sides are equal)
(Equilateral Triangle is all sides are equal)
(Scalene Triangle is all sides are different)'''
# A = int(input("Enter A Side : "))
# B = int(input("Enter B Side : "))
# C = int(input("Enter C Side : "))
# if A == B == C :
#     print("Equilateral Triangle")
# elif A==B or A==C or B==C :
#     print("Isosceles Triangle")
# else :
#     print("Scalene Triangle")


'''Write a program to implement the company policy followed by a company to process customer orders is given by the following rules: 
(a)  If  a  customer  order  is  less  than  or  equal  to  that  in  stock and has credit is OK, supply has requirement. 
(b)  If has credit is not OK do not supply. Send him intimation. 
(c)  If  has  credit  is  Ok  but  the  item  in  stock  is  less  than  has order,  supply  what  is  in  stock. Intimate  to  him  data  the balance will be shipped. '''
# print("The price Per stock is 100rs")
# stock = int(input("Enter the stock: "))
# order = int(input("Enter Your order: "))
# credit = int(input("Enter Your Credit: "))
# if order <= stock and credit >= (100 * order):
#     print("Your order will be deliverd shortly")
# elif order <= stock and credit < (100 * order):
#     print("Insufficient Credit")
# elif order > stock and credit >= (100 * order):
#     print("Your remaining order will be deilvered shortly")


'''Write a Python program to read temperature in centigrade and display a suitable message according to the temperature state below: 
a) Temp < 0 then Freezing weather 
b) Temp 0-10 then Very Cold weather 
c) Temp 10-20 then Cold weather 
d) Temp 20-30 then Normal weather 
e) Temp 30-40 then Its Hot weather
f) Temp >=40 then Its Very Hot weather'''
# Temp = float(input("Enter Current Temperature : "))
# if Temp < 0 :
#     print("Freezing weather")
# elif Temp <= 10 :
#     print("Very cold weather")
# elif Temp <= 20 :
#     print("Cold weather")
# elif Temp <= 30 :
#     print("Normal weather")
# elif Temp <= 40 :
#     print("Hot weather")
# else :
#     print("Its very hot weather")

