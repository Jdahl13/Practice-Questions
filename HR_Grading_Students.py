import math
import random
#Question synposis is as follows
#us a list to hold ints that represent studnet grades, the professor is willing to bump up grades if they
#are less than 3 points away from the next multiple of 5 of that num (83 ->85, etc). If the grade is less than 50
# there is no rounding as this is a fail. grades must be 0-100 

grades = []
for grade in range(6): 
    grades.append(random.randint(40,100))
def adjustGrades(gradeList):
    'takes list of grades and determines if rounding is appropriate'
    updatedGrades = []
    for grade in gradeList:
        old = grade
        updated = 0
        new = 0
        if grade < 40:
            updatedGrades.append(grade)
        updated = old - (old % 5) + 5
        new = updated - old
        if new < 3:
            updatedGrades.append(updated)
        else:
            updatedGrades.append(grade)
    return updatedGrades
print(grades)
finalGrades = adjustGrades(grades)
print(finalGrades)
    
        
#print(grades)