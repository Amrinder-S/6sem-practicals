import csv
import math

def calculateEntropy(x, y):
    if x == 0 or y == 0:
        return 0
    entropy = -(x / (x + y)) * math.log2((x / (x + y))) - (y / (x + y)) * math.log2((y / (x + y)))
    return entropy

def calculateInformationGain(data, title, entropyWhole, count):
    value_counts = {}
    for row in data:
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
        informationGain += (counts['yes'] + counts['no']) * calculateEntropy(counts['yes'], counts['no']) / count
    informationGain = entropyWhole - informationGain
    return informationGain

# Read CSV file and store its contents in a list of dictionaries
with open('decision_tree.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

def decisionTree(data):
    yes = sum(1 for row in data if row['PlayTennis'] == 'yes')
    no = sum(1 for row in data if row['PlayTennis'] == 'no')
    entropyWhole = calculateEntropy(yes, no)
    informationGains = {}
    for title in data[0].keys():
        if title != 'PlayTennis':
            informationGains[title] = calculateInformationGain(data, title, entropyWhole, yes + no)
    max_key = max(informationGains, key=lambda k: informationGains[k])
    print("Maximum Information Gain Attribute:", max_key)
    print("Information Gains:", informationGains)

    # Split data based on the maximum information gain attribute
    split_data = {}
    for row in data:
        attribute_value = row[max_key]
        if attribute_value not in split_data:
            split_data[attribute_value] = []
        split_data[attribute_value].append(row)

    # Print or return split data
    for value, subset in split_data.items():
        print(f"Data subset for {max_key} = {value}:")
        subset_labels = set(row['PlayTennis'] for row in subset)
        if len(subset_labels) == 1:
            print(f"All 'PlayTennis' values in this subset are: {subset_labels.pop()}")
        else:
            for row in subset:
                print(row)

    return split_data

# Assuming 'data' is already defined and populated with your dataset
split_data = decisionTree(data)


# decisionTree(data)