import sys

def input_receiver():
    txt = input("Enter x1,x2 digits, seperated by comma  ")
    x_first_list = txt.split(',')
    if( len(x_first_list) != 2):
        print("invalid input for x1, x2. Input should be 2 digits seperated by comma")
        sys.exit()

    txt = input("Enter x3,x4 digits, seperated by comma  ")
    x_second_list = txt.split(',')
    if( len(x_second_list) != 2):
        print("invalid input for x3,x4. input should be 2 digits seperated by comma")
        sys.exit()
    print(overlap_computer(x_first_list, x_second_list))


def overlap_computer(x_first_list, x_second_list):

    x1 = x_first_list[0]
    x2 = x_first_list[1]

    x3 = x_second_list[0]
    x4 = x_second_list[1]
    #i want the x2 figure to always be greater than x1 so the generate range can be in an absolute order,
    #same for x3 and x4 
    if(x1 > x2):
        temp = x2
        x2 = x1
        x1 = temp

    if(x3 > x4):
        temp = x4
        x4 = x3
        x3 = temp

    x1_x2_list = list(range( int(x1),   int(x2)+1 ))
    x3_x4_list = list(range( int(x3),   int(x4)+1 ))

    for x1_cordinates in x1_x2_list:
        for x2_cordinates in x3_x4_list:
            if(x2_cordinates == x1_cordinates):
                return ("THERE IS AN OVERLAP")
                
        
    return ("THERE IS NO OVERLAP")


if __name__ == "__main__":
    input_receiver()