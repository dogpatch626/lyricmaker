import pprint
pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")

l = []
#i = 0
r = 1
for x in f:
    l.append(int(x))
    
f.close()
    #i+= 1
# find sum of 2020
#modular math? prolly not
left = 0
right = 0
middle = 0 # left and right side of the equatino aux space
#g = int(l[0])
#print(g)
# bleh naive solutin O(n^2)
for i in range(0, len(l)-1):
    #iterate through subtracting each number from 2020 and then see if the remainder is in the lsit 
    left  = l[i]
    #print("l")
    #pp.pprint(  left  )
    #print("m")
    middle = l[i+1]  
   # pp.pprint(middle)
   # print(middle)
   # print("fnd")
    fnd  = middle + left
    if(fnd <= 2000):
        pp.pprint(fnd)
    right = 2020 - fnd
   
   # print(right)
    try:
        #pp.pprint(l.index(fnd))
        pp.pprint(l.index(right))
        pp.pprint(left * right * middle  )
        pp.pprint(left + right + middle )
    except ValueError:
        g = 1
    


   



