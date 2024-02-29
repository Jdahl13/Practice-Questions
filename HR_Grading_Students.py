import math
import random
#Question synposis is as follows
#us a list to hold ints that represent studnet grades, the professor is willing to bump up grades if they
#are less than 3 points away from the next multiple of 5 of that num (83 ->85, etc). If the grade is less than 50
# there is no rounding as this is a fail. grades must be 0-100 

grades = []                                 # blank grade book
for grade in range(6):                      #fill with grades
    grades.append(random.randint(40,100))
def adjustGrades(gradeList):
    'takes list of grades and determines if rounding is appropriate'
    updatedGrades = []                      # new list to hold grades after rounding is determined
    for grade in gradeList:
        old = grade
        updated = 0
        new = 0
        if grade < 40:                      # auto failure, no need to check if it can be rounded
            updatedGrades.append(grade)
        updated = old - (old % 5) + 5       # find the next multiple of 5 after number
        new = updated - old
        if new < 3:                         #determine if meets rounding criteria
            updatedGrades.append(updated)
        else:
            updatedGrades.append(grade)
    return updatedGrades
print(grades)                               #before gradebook
finalGrades = adjustGrades(grades)          
print(finalGrades)                          #after function is run 
    
        
#This seems to solve the question! Furture things to add, checking if gradebook has values in range
#can probably optimize this to reduce code