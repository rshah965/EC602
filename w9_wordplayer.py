# Author Rishab Shah rishah@bu.edu

import sys

with open(sys.argv[1]) as f:
    il = f.read().split()
d = {}

for i in il:
    d.setdefault(len(i), {})
    d[len(i)].setdefault(''.join(sorted(i)), [])
    d[len(i)][''.join(sorted(i))].append(i)
while(True):
    x = input()
    y = x.split()
    z = int(y[1])
    if z == 0:
        sys.exit(0)
    res = []

    y1 = ''.join(sorted(y[0]))
    if z not in d:
        print('.')
    else:
        if (len(y1) == z):
            if (y1 in d[z]):
                for i in d[z][y1]:
                    res.append(i)
        else:
            for i in d[z]:
                tmp = i
                for j in y1:
                    if (len(tmp) != 0 and j == tmp[0]):
                        tmp = tmp[1:]
                if len(tmp) == 0:
                    for k in range(len(d[z][i])):
                        res.append(d[z][i][k])
        for i in sorted(res):
            print(i)
        print('.')
