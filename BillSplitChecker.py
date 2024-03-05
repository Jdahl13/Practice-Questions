#Bill and Anna spit their check. Anna will only pay for items she ordered. Function checks to see if Bill's calc
#is correct or not. Input provided will be a list that reps the "Bill", a number that includes what anna didnt 
#eat, and Bills calculation. If the calc matches the true split, print "Correct"
import random

def billChecker(bill, annasBill, billsEstSplit):
    'checks to see if Bill is correctly calculating the bill split'
    x = billsEstSplit
    y = annasBill
    if x == y:
        print("Bill's suggested split is correct!")
    else:
        print("Bill's wants Anna to pay her unfair share")
    
    
#Set up bill
bill = []
sizeOfBill= random.randint(1,10)
for item in range(0,sizeOfBill):
    item = random.randint(0,50)
    bill.append(item)


#set up anna and if she will have anything to remove
annasIndexToRemove = 0
x = random.randint(1,2)
if x == 1:
    print("Anna does not split everything on the bill")
    annasIndexToRemove = random.randint(1,len(bill)-1)
else:
    print("Anna splits everything on the bill")

#generate Bill's est split
split = 0
for item in range(len(bill)):
    item = bill[item]
    split += item
split = split/2
print(split)

#generate anna's split if different
annaSplit = 0
if annasIndexToRemove > 0:
    bill.remove(bill[annasIndexToRemove])
for item in range(len(bill)):
    item = bill[item]
    annaSplit += item
annaSplit = annaSplit / 2

billChecker(bill, annaSplit, split)







#driver code:





