# A function to determine if it is true or false - Boolean (Bool)
from ast import Num


def divisible(numerator: int, denominator: int)->bool:
    # "equal to 0 (zero)". - When the division returns a zero it will be true other wise false 
    return numerator % denominator == 0 
#Divide 30/5 is true 30/4 is false
print(divisible(30,5))

#--------------------------------------------------------------------------------------

def find_num(number_list: list, number: int)->bool: 
    for iterate_number in number_list: 
        if iterate_number == number: 
            return True 
    else: 
        #pass - instead of pass here we can return False if it is indeed false. 
            return False 
    
result = find_num([1,2,3,4,5,6,7,8,9], 9) 
print(result)

# Briefly explain and comment this code. Why do you get the value None? - It was set to pass rather than return False if it was False
# What values in the final statement will result in the function returning True? Why?- Adding the digit 9 within the square brackets returned the value trus
# Can you modify this function to return False instead of None if the value is not found? - Yes completed.

#--------------------------------------------------------------------------------------
print("Write a function to search for an even number in a list of numbers.") 
# Return True if you find an even number. Return False if you do not.

def user_input_checking_even_number_list(user_input_list):
    for input_number in user_input_list:
        if input_number%2 == 0:
            return True
        else:       
            return False

    Result = oddeven_number([1,3,5,8,9,11,20,21])
    print(result)

#--------------------------------------------------------------------------------------
print("Write a lambda function to calculate the volume of a cylinder")
circumference = lambda radius : 2 * 3.142 * radius 
area = lambda radius : 3.142 * radius * radius 
radius = 5 
print(circumference(radius), area(radius))
#--------------------------------------------------------------------------------------