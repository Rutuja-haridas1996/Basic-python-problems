'''
Problem Statement:
Write a function that computes the volume of a sphere when passed the radius.  
Use an assert statement to test the function.
'''

def sphere_volume(radius):
    try:
        assert isinstance(radius,int) or isinstance(radius,float)
        return ((4/3)*(3.14))*(radius**3)
    except AssertionError as ae:
        return 'Invalid radius'

print(sphere_volume(63))