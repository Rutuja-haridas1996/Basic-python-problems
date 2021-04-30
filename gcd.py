'''
Problem Statement:
Find the greatest common divisor between two numbers.
Write a function.  Make sure to put error checking in the function.
Both numbers must be positive integers for the function to work.
'''

def gcd(num1,num2):
    try:
        assert (
            (isinstance(num1,int) or isinstance(num1,float)) and (
                isinstance(num2,int) or isinstance(num2,float)
                ) and (num1 >= 0 and num2 >=0)
        )
        for i in range(1,min(num1,num2)):
            if ((num1 % i) == 0 and (num2 % i) == 0):
                gcd = i
        return 'GCD of {num1} and {num2}  : {gcd}'.format(num1=num1,num2=num2,gcd=gcd) 

    except AssertionError as ae:
        return 'Invalid numbers to compute gcd'

print(gcd(10,20))