'''
Problem Statement:
7.Use the print statement to write your initials of your name to the screen using * symbol.
Make a large string with line breaks. 
'''

def name_initials(full_name):
    splited_name_list = full_name.split()
    intial_name = '*'.join([name[0] for name in splited_name_list])
    return intial_name
    
name_initials('Rutuja Haridas')