'''
Problem Statement:
9.Write a function that take a upper limit as a parameter and returns a list of prime numbers. 
Put it in a module and use the function to generate all the prime number less than 200.
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