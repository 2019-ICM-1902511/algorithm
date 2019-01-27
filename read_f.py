import numpy as np
import csv

path = "data/test.csv"
l0 = []
l1 = []
li = []
with open(path) as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
        if line == []:
            l1.append(l0)
            l0 = []
            continue
        for i in line:
            if "/" in i:
                if " " in i:
                    b = i.split("/")
                    c = b[0].split(" ")
                    li.append(int(c[0]) + int(c[1]) / int(b[1]))
                else:
                    b = i.split("/")
                    li.append(int(b[0]) / float(b[1]))
            else:
                li.append(float(i))
        l0.append(li)
        li = []
    l1.append(l0)
print(l1)
