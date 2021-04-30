'''
Problem Statement:
Take generic input with the input command.
Use an if statement to write a function that returns “Lamar is a great school” 
if the sentence passed has the word Lamar. 
'''

def check_lamar_exists_statment(statement):
    try:
        assert 'Lamar' in statement 
        if 'Lamar' in statement:
            return 'Lamar is a great school'
    except AssertionError as ae:
        return 'Lamar should be in statement'


input_statement = input('Enter statement: ')
print(check_lamar_exists_statment((input_statement)))


