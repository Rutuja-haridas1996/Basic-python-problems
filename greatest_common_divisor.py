'''
Problem Statement:
10.Find the greatest common divisor between two numbers.  Write a function.  
Make sure to put error checking in the function.  
Both numbers must be positive integers for the function to work.
'''

def isprime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
        
def get_prime_numbers(upper_limit):
    try:
        assert isinstance(upper_limit,int) or isinstance(upper_limit,float)
        prime_number_list = []
        for num in range(1,upper_limit+1):
            # Check if number is prime or not
            if isprime(num):
                prime_number_list.append(num)
        
        return prime_number_list

    except AssertionError as ae:
        return 'Invalid upper limit'

print(get_prime_numbers(5))