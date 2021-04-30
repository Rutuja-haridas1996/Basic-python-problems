'''
Problem Statement:
8.Write a function that computes the average of numbers input by the user and displays 
the average, minimum, maximum and the numbers in a nice format (using print statement).
'''

def number_calculations(numbers):
    try:
        assert all((isinstance(number,int) or isinstance(number,float)) for number in numbers)
        average = sum(numbers)/len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)

        return f'''
                Average of numbers is {average},
                Minimim of numbers is {minimum},
                Maximum of numbers is  {maximum}
                '''
    except AssertionError as ae:
        return 'Invalid number list'


print(number_calculations([10,50]))