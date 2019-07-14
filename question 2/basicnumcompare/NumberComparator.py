class NumberComparator():
 
    def __init__(self, first, second):
        self.first_digit_input = first
        self.second_digit_input = second


    
    def greater_than(self):
        first_digit = float( self.first_digit_input)
        second_digit = float( self.second_digit_input)

        if(first_digit > second_digit):
            return True
        else:
            return False
    
    def less_than(self):
        first_digit = float( self.first_digit_input)
        second_digit = float( self.second_digit_input)

        if(first_digit < second_digit):
            return True
        else:
            return False
    
    def equal_to(self):
        first_digit = float( self.first_digit_input)
        second_digit = float( self.second_digit_input)

        if(first_digit == second_digit):
            return True
        else:
            return False
            
    