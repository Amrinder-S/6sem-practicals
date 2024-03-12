import csv
import math
import tkinter as tk
from tkinter import ttk

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

def create_decision_tree(data, parent_node=None, parent_attribute=None):
    # Calculate entropy for the current subset
    yes_count = sum(1 for row in data if row['PlayTennis'] == 'yes')
    no_count = sum(1 for row in data if row['PlayTennis'] == 'no')
    entropy = calculateEntropy(yes_count, no_count)

    # Check if the subset is pure
    if yes_count == 0:
        leaf_label = 'no'
        if parent_node is not None:
            parent_node[parent_attribute] = leaf_label
        return
    elif no_count == 0:
        leaf_label = 'yes'
        if parent_node is not None:
            parent_node[parent_attribute] = leaf_label
        return

    # Calculate information gains for attributes
    information_gains = {}
    for title in data[0].keys():
        if title != 'PlayTennis':
            information_gains[title] = calculateInformationGain(data, title, entropy, yes_count + no_count)

    # Choose the attribute with maximum information gain
    max_attribute = max(information_gains, key=lambda k: information_gains[k])

    # Create root node if this is the first call
    if parent_node is None:
        root_node = {max_attribute: {}}
        create_decision_tree(data, root_node, max_attribute)
        return root_node

    # Create child nodes for the selected attribute
    parent_node[parent_attribute] = {max_attribute: {}}
    split_data = {}
    for row in data:
        attribute_value = row[max_attribute]
        if attribute_value not in split_data:
            split_data[attribute_value] = []
        split_data[attribute_value].append(row)

    # Recursively call create_decision_tree for each subset
    for value, subset in split_data.items():
        create_decision_tree(subset, parent_node[parent_attribute], value)

# Read CSV file and store its contents in a list of dictionaries
with open('decision_tree.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create the decision tree
root_node = create_decision_tree(data)

# Create a Tkinter window
root = tk.Tk()
root.title("Decision Tree Visualization")

# Function to recursively build the treeview
def build_tree(tree, node, label=""):
    if isinstance(node, dict):
        for attribute, children in node.items():
            subtree = tree.insert(label, "end", text=attribute)
            build_tree(tree, children, subtree)
    else:
        tree.insert(label, "end", text=node)

# Create a Treeview widget to display the decision tree
tree = ttk.Treeview(root)
tree.heading("#0", text="Decision Tree")
build_tree(tree, root_node)
tree.pack(expand=True, fill="both")

root.mainloop()
