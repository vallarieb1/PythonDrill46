for i in range(4):
    print(i)

def list_multiply ():
    numlist = [1000,100,10]
    numrange = [i for i in range (3,0,-1)]
    num_Total = (numlist[0]*numrange[0])+(numlist[1]*numrange[1])+(numlist[2]*numrange[2])
    print ("\nHere is the answer for Python 46 of 68, Drill #2: ",num_Total)

list_multiply()

#or use below, where end="" in the print() function means to print on the same line.
for i in range(3,-1,-1):
    print(i,end="")

def list_multiply2 ():
    numlist2 = [1000,100,10]
    numrange2 = [n for n in range (8,0,-2)]
    num_Total2 = (numlist2[0]*numrange2[0])+(numlist2[1]*numrange2[1])+(numlist2[2]*numrange2[2])+(numrange2[3])
    print ("\nHere is the answer for Python 46 of 68, Drill #3: ",num_Total2)

list_multiply2()

#or use below, where end="" in the print() function means to print on the same line.
for i in range(8,0,-2):
    print(i,end="")




    






    
