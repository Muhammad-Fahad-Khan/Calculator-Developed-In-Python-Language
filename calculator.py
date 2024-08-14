# hii everyone 
# today we are going to learn about how to create a calculator code in Python Language.

# Stay together to learn about some thing new
# Hope You Will Enjoy & Learn From This code

import math   #This is for square we will learn next

print(""" Select Operation Which you want To Do in Calculator:
1. Add
2. Subtract
3. Multiple
4. Divide
5. Square of Number ^2
6. Square_Root
7. Reminder of Number AKA Modulas\n""")

# Opt = Option which we use to give in code
opt = int(input("Enter Above No." ))
# this will onlt accept numeric Numbers like 1,2,3,4,5, etc.


# we use if else statement bcz of these only 3 option bcz they accept only one num at a time
if opt  in [5,6,7]:        
    num1 = int(input("Enter Number: "))

    match opt:
        case 5:
            sq = num1 ** 2
            print(f'The Square of {num1} is: {sq}')   
            #this f'' is called F function statement will allow user to write like human language but this is some concept which u have to understand like {num1} it allow to print value of variable.


        case 6:
            sqroot = math.sqrt(num1)
            print(f'The Square Root(Under Root) of {num1} is: {sqroot}')

        case 7:
            rem = num1 % 2
            print(f"The Reminder of {num1} is: {rem}")

#Now we will Write else function code in which we enter 2 numbers to perform action.

else:
    #Declare & Assigning Value of variable and also it allow user to enter value

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print(f'You Enter first number is {num1} & second number is {num2}.')

    # now we Use the match-case structe also it is known as Switch case in C++ Language. :)

match opt:
    case 1:
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}")

    case 2:
        sub= num1 - num2
        print(f"{num1} - {num2} = {sub}")    # after copy paste of same code, also change sign after paste of that code

    case 3 :
         mul = num1 * num2
         print(f"{num1} * {num2} = {mul}")

    case 4:
        # this will allow user to not enter zero for number. It can't be divide by zero  
        if num2!=0: 
                div = num1 / num2
                print(f"{num1} / {num2} = {div}")
        else:
            print("Error Because of Zero in Denominator. Thank You!!!!!")



                                                    # THANK YOU For Watching.