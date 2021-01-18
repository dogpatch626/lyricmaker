import pprint

pp = pprint.PrettyPrinter(indent=4)
f = open("input.txt", "r")

l = []

for x in f:
    l.append(x)
s = ""
# pp.pprint(l[10])
# if l[10][1].isdigit():
#     s = l[10][0] + l[10][1]
# polIndex = l[0].index(":") - 3
# print(l[0][polIndex])
# print(s)
# x = 0
upper = 0
lower = 0
g = 0
for i in range(0, len(l)):
    # figure out what the lower bound is

    if l[i][1].isdigit():
        s = l[i][0] + l[i][1]
        lower = int(s)
    else:
        lower = int(l[i][0])
        # figure out upper
    # if l[i][2].isdigit() and l[i][3].isdigit():
    upperIndex = l[i].index(":") - 3
    if l[i][upperIndex - 1].isdigit():
        rep = l[i][upperIndex - 1] + l[i][upperIndex]
        upper = int(rep)
        # replace = l[i][2] + l[i][3]
    else:
        # pp.pprint(l[i][2])
        upper = int(l[i][upperIndex])

    pollIndex = l[i].index(":") - 1
    pol = l[i][pollIndex]
    if (l[i].count(pol) - 1) >= lower and (l[i].count(pol) - 1) <= upper:
        g += 1
print(g)
