import sys
from NumberComparator import NumberComparator

# def checkIfNumber(user_input):
#     try:
#         return float(user_input)
        
#     except ValueError:
#         print("Oops! Please enter valid numbers")

        

# def numberComparator(first_digit_input, second_digit_input):
#     first_digit = float( first_digit_input)
#     second_digit = float( second_digit_input)

#     if(first_digit > second_digit):
#         return (str(first_digit_input)+ " is greater than "+ str(second_digit_input))
        
#     elif(first_digit == second_digit):
#         return (str(first_digit_input)+ " is equal to "+ str(second_digit_input))
        
#     else:
#         return (str(first_digit_input)+ " is less than "+ str(second_digit_input))
  

if __name__ == "__main__":
    try:
       
        first_digit_input = input("Enter the first digit ")        
        second_digit_input = input("Enter the second digit ")

        comparison =  NumberComparator( first_digit_input, second_digit_input)

        if(comparison.greater_than() == True):
            print (str(first_digit_input)+ " is greater than "+ str(second_digit_input))
        
        if(comparison.less_than() == True):
            print (str(first_digit_input)+ " is less than "+ str(second_digit_input))
  
        if(comparison.equal_to() == True):
            print (str(first_digit_input)+ " is equal to "+ str(second_digit_input))
  



    except ValueError:
        print("Oops! please enter valid digits") 



  





    

