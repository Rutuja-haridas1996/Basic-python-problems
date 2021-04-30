'''
Problem Statment:
Sum the numbers from 1 to 100 using a loop and the range statement.

We can solve this problem using two ways:

1. Pythonic way: 
sum(list(range(1,101))) --> Which will first get list of all elements between 1-100 
and then use for loop to sum them, but it will be loop for 100 times with complexity O(n), which
is not an optimistic way

2. Formula:
sum = ((end * (end + 1)) - (start * (start - 1))) / 2 
'''

def get_sum(start, end):
    sum = ((end * (end + 1)) - (start * (start - 1))) / 2 
    return sum

print(get_sum(-41,-455))

