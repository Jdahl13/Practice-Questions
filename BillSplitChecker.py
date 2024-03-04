#Bill and Anna spit their check. Anna will only pay for items she ordered. Function checks to see if Bill's cal
#is correct or not. Input provided will be a list that reps the "Bill", a number that includes what anna didnt 
#eat, and Bills calculation. If the calc matches the true split, print "Correct"
import random

def billChecker(bill,annasSubtractions,billsCalc):
    'take 3 inputs to check if Bills calc for split is correct'
    
    
    
    

#Set up bill
bill = []
sizeOfBill= random.randint(1,10)
for item in range(0,sizeOfBill):
    item = random.randint(0,50)
    bill.append(item)


#set up anna and if she will have anything to remove
x = random.randint(1,2)
if x == 1:
    print("Anna splits everthing on the bill")


#driver code:
print(bill) 


