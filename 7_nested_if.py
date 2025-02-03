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
# Hardness = int(input("Enter the Hardness: "))
# Carbon_content = float(input("Enter the Carbon Content: "))
# Tensile_strength = int(input("Enter the Tensile Strength: "))
# hh = False
# cc = False
# ts = False
# if Hardness > 50:
#     hh = True
# if Carbon_content < 0.7:
#     cc = True
# if Tensile_strength > 5600:
#     ts = True
# if hh == True and cc == True and ts == True:
#     print("Grade of Steel is 10")
# elif hh == True and cc == True and ts == False:
#     print("Grade of Steel is 9")
# elif hh == False and cc == True and ts == True:
#     print("Grade of Steel is 8")
# elif hh == True and cc == False and ts == True:
#     print("Grade of Steel is 7")
# elif hh == True or cc == True or ts == True:
#     print("Grade of Steel is 6")
# else:
#     print("Grade of Steel is 5")


'''Write a program that asks the user to enter a year. Determine whether the
year is a leap year or not. If it is a leap year, display "Leap year." Otherwise, 
display "Not a leap year." (Leap years are divisible by 4, but not divisible by 
100 unless they are also divisible by 400.)'''
''' Century year - 2000 1200 1800 1900 1600 % 100 % 400 '''
''' Non-Century year - 2024 2023 1991 2014 2012 % 4 '''
# year = int(input("Enter any Year: "))
# if year % 100 == 0: 
#     if year % 400 == 0:
#         print("Leap year and a Century year")
#     else:
#         print("Century year not a leap year")
# else:
#     if year % 4 == 0:
#         print("Leap year and non-century year")
#     else:
#         print("Non-centruy year not a leap year")


'''Write a program to take input of three number and check which is greatest.'''
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if a > b:
#     if a > c:
#         print(f"{a} is greatest")
#     else:
#         print(f"{c} is greatest")
# else:
#     if b > c:
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")