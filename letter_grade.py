'''
Problem Statement: 
Write a function that returns the letter grade based on an input number grade. 
This is a simple if statement.  If x is greater than or equal to 90 return A and so on.  
Write the function and demonstrate that it works with by running it.  
Add assert statement after your demonstration to show how you can test something.

90-100, 89-80, 79-60, 59-40, 0-39  
A        B      C      D     F
'''

# Dictonary for letter grades based on their marks from low-high
letter_grades = {
    'A' : {
        'low' : 90,
        'high' : 100
    },
    'B' : {
        'low' : 80,
        'high' : 89
    },
    'C' : {
        'low' : 60,
        'high' : 79
    },
    'D' : {
        'low' : 40,
        'high' : 59
    },
    'F' : {
        'low' : 0,
        'high' : 39
    }
}

def get_letter_grade(marks):
    try:
        if round(float(marks)) < 0 or round(float(marks)) > 100:
            return 'Entered incorrect number of grades'

        grade_obtained = [grade[0] for grade in letter_grades.items()
                    if (grade[1]['low']) <= round(float(marks)) <= (grade[1]['high'])
        ][0]
        return 'Grade obtained by student {}'.format(grade_obtained)
    except ValueError as t:
        # This will be the case when string is entered as input
        return 'Invalid marks entered'

marks = input('Enter marks: ')
print(get_letter_grade((marks)))



