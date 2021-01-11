import pprint
pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")

l = []
#i = 0
for x in f:
    l.append(int(x))
f.close()
    #i+= 1
# find sum of 2020
#modular math? prolly not
left = 0
right = 0 # left and right side of the equatino aux space
#g = int(l[0])
#print(g)
# bleh naive solutin O(n^2)
for i in l:
    #iterate through subtracting each number from 2020 and then see if the remainder is in the lsit 
    left  = int(i)
    right = 2020 - int(i); 
    try:
        pp.pprint(l.index(right))
        pp.pprint(left * right, " {i}")
        pp.pprint(left + right, " {i}")
    except ValueError:
        g = 1
    try:
        l.index(left)
    except ValueError:
       g = 1
    #pp.pprint(right)
    # if str(left) in l:
    #     print(left*right)
    # else:
    #     print("fk off")   
    #pp.pprint(right)

        





# im too tired for this 


#pp.pprint(l)