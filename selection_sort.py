'''
Problem Statement:
a. Sort a list of numbers using the sort function and by code that you write yourself. 
Please do a simple selection sort. 

b. Find the minimum item on the original list and move to position 1.
Repeat this until the list is sorted.This algorithm is not effluent but is good for teaching. 
If you can do this task you understand python lists and loops.  No need to place in a function. 
Test on an example at least 5 integers in a list. 
'''

def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x,y

# b.
def sort_list(number_list):
    for i in range(len(number_list)):
        min_index = i
        for j in range(i+1,(len(number_list))):
            if number_list[i] > number_list[j]:
                min_index = j
        
        swap_output = swap(number_list[i],number_list[min_index])

        # number_list[i],number_list[min_index] = number_list[min_index], number_list[i]
        # swap_output = swap(1,2)
        print(swap_output)
            
    # print(number_list)


def check_min(number, number_list):
    return min(number_list)

sort_list([40,42,4])
swap(10,-50)