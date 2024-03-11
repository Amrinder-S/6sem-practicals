from sklearn.datasets import load_iris
import pandas as pd
import math
n = int(input("Enter No Of Neighbors: "))
iris_data = load_iris()
iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
input_params = iris.columns

tar_type = ["Sentosa", "Versicolor","Virginica"]
iris["target"] = iris_data.target
iris["distance"] = 0
dist = 0
input_data = [float(input(f"Enter {param}: ")) for param in input_params]
for index,row in iris.iloc[:,:-2].iterrows():
    # print(row)
    for i,val in enumerate(row):
        # print(i)
        dist = dist +  (val - input_data[i] )**2
    iris["distance"] = math.sqrt(dist)
    dist = 0
sorted = iris.sort_values(by="distance")
neighbors = sorted["target"].iloc[:n].tolist()

result = max(set(neighbors), key = neighbors.count)


print(tar_type[result])