import math
import random
#Question synposis is as follows
#us a list to hold ints that represent studnet grades, the professor is willing to bump up grades if they
#are less than 3 points away from the next multiple of 5 of that num (83 ->85, etc). If the grade is less than 50
# there is no rounding as this is a fail. grades must be 0-100 

grades = []
for grade in range(6): 
    grades.append(random.randint(40,100))

print(grades)