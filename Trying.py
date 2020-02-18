'''
M = 7
N = 9
P = 3
Q = 5
'''
'''
'''
import numpy as np
M = int(input("Enter lengths of M"))
N = int(input("Enter lengths of N"))
P = int(input("Enter breadths of P"))
Q = int(input("Enter Breadth of q"))
global count
count = 0
Lengths = [M,N]
Breadths = [P,Q]
Outcomes = []
global Modified_Size
Modified_Size = 0
def Cadbury(k):
    global count
    global Modified_Size
    Minimum_Element = min(k)#3
    Outcomes.append((Minimum_Element,Minimum_Element))#(3,3)
    Values = [Minimum_Element,Minimum_Element]#3,3
    if (k[0] > k[1]):#5>4
        Modified_Size = np.subtract(k,(Minimum_Element,0))## (6,3) - (3,0) (3,3)
    elif (k[0] < k[1]):
        Modified_Size = np.subtract(k,(0,Minimum_Element))
    if (Modified_Size[0]== Modified_Size[1]):
        count = count + 1
    if (Modified_Size[0] != Modified_Size[1]):
        Minimum_Element = Modified_Size.min()
        if (Minimum_Element == 1):
            MaxElement = int (Modified_Size.max())
            count = count + MaxElement
        else:
            Cadbury(tuple(Modified_Size))

for i in Lengths:
    for j in Breadths:
        Cadbury((i,j))
print ("No of possible Outcomes are",len(Outcomes)+count)
