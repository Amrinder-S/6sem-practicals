import csv
import math

def calculateEntropy(x, y):
    if x == 0 or y == 0:
        return 0
    entropy = -(x / (x + y)) * math.log2(x / (x + y)) - (y / (x + y)) * math.log2(y / (x + y))
    return entropy

def calculateInformationGain(entropy_whole, data, attribute_index):
    values = set([row[attribute_index] for row in data])
    entropy_attribute = 0
    for value in values:
        subset = [row for row in data if row[attribute_index] == value]
        yes_count = sum(1 for row in subset if row[-1] == 'yes')
        no_count = len(subset) - yes_count
        entropy_attribute += (len(subset) / len(data)) * calculateEntropy(yes_count, no_count)
    information_gain = entropy_whole - entropy_attribute
    return information_gain

# Read data from CSV
data = []
with open("decision_tree.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip headers
    for row in reader:
        data.append(row)

# Calculate overall entropy
yes_count = sum(1 for row in data if row[-1] == 'yes')
no_count = len(data) - yes_count
entropy_whole = calculateEntropy(yes_count, no_count)
print(f"Entropy for whole dataset: {entropy_whole}")

# Calculate information gain for each attribute
titles = ["Outlook", "Temp", "Humidity", "Wind"]
for i, title in enumerate(titles):
    information_gain = calculateInformationGain(entropy_whole, data, i)
    print(f"Information Gain for {title}: {information_gain}")
