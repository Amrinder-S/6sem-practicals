import csv
import math
yes = 0
no = 0
x = csv.reader(open("decision_tree.csv", "r"))

for i in x:
    if(i[len(i)-1]=='yes'):
        yes = yes + 1
    elif(i[len(i)-1]=='no'):
        no = no + 1
entropy = -(yes/(yes+no))*math.log2((yes/(yes+no))) - (no/(yes+no))*math.log2((no/(yes+no)))
print(entropy)