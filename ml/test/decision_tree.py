import csv
import math
def calculateEntropy(x,y):
    if(x==0 or y==0):
        return 0
    entropy = -(x/(x+y))*math.log2((x/(x+y))) - (y/(x+y))*math.log2((y/(x+y)))
    return entropy

def calculateInformationGain(title, entropyWhole, count):
    value_counts = {}
    with open('decision_tree.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row[title]
            play_tennis = row['PlayTennis']
            if value not in value_counts:
                value_counts[value] = {'yes': 0, 'no': 0}
            if play_tennis == 'yes':
                value_counts[value]['yes'] += 1
            else:
                value_counts[value]['no'] += 1
    informationGain = 0
    for value, counts in value_counts.items():
        informationGain = informationGain + (counts['yes']+counts['no'])*calculateEntropy(counts['yes'],counts['no'])/count
    informationGain = entropyWhole - informationGain
    # print(f"Information gain for {title}:{informationGain}")
    return informationGain


yes = 0 # Initializing yes and no values as 0.
no = 0

for i in csv.reader(open("decision_tree.csv", "r")):
    if(i[len(i)-1]=='yes'):
        yes = yes + 1
    elif(i[len(i)-1]=='no'):
        no = no + 1

with open('decision_tree.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    titles = next(reader)[:-1]

entropyWhole = calculateEntropy(yes,no)
print(calculateEntropy(yes,no))

informationGains = {}
for title in titles:
    informationGains[title] = calculateInformationGain(title, entropyWhole, yes+no)
print(informationGains)
max_key = max(informationGains, key=lambda k: informationGains[k])
print(max_key)
