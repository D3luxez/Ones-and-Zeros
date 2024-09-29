#Program to find a number of zero bits and one bit present in a number
#Function taking our number as input 
def numberofbits(n):
    ones = 0
    Zeros = 0

#While our number is greater than zero check last bit and right shift
    while(n):
        #Use AND operator to check if last bit is one or 0
        if(n & 1 == 1):
            ones += 1
        else:
            Zeros += 1
        #Right shift the number remove the last bit thate we just met
        n >>= 1
        print("\n \ones =", ones, "\n Zeros", Zeros)
number = int(input("Enter your name"))
numberofbits (number)