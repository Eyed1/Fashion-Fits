from sklearn.ensemble import RandomForestRegressor 
import json
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

data_file = open("train_data.jsonl", "r")
data_objs = []
for row in data_file:
    data_objs.append(json.loads(row))

#x_train3 = pd.DataFrame(columns = ["inner top", "outer top", "bottom"])
x_train_arr_2 = []
x_train_arr_3 = []
y_train_arr2 = [] 
y_train_arr3 = []

for combo in data_objs:
    arr = combo["datapoint"]
    val = combo["util"]
    if (len(arr) == 2):
        x_train_arr_2.append(arr) 
        y_train_arr2.append(val)
    if (len(arr) == 3):
        x_train_arr_3.append(arr) 
        y_train_arr3.append(val)

y_train2 = np.array(y_train_arr2)
y_train3 = np.array(y_train_arr3)
x_train2 = pd.DataFrame(np.array(x_train_arr_2), columns = ["top", "bottom"])
x_train3 = pd.DataFrame(np.array(x_train_arr_3), columns = ["inner top", "outer top", "bottom"])


print("STAGE 1")
regressor2 = RandomForestRegressor(n_estimators = 100, max_depth = 10)
#print(len(x_train2), len(y_train2))
regressor2.fit(x_train2, y_train2)
regressor3 = RandomForestRegressor(n_estimators = 100, max_depth = 10)
#print(len(x_train2), len(y_train2))
regressor3.fit(x_train3, y_train3)

print("END")

#model2 = pickle.dumps(regressor2)
#model3 = pickle.dumps(regressor3)

outfile2 = open("regressor_size2.pkl", "wb")
outfile3 = open("regressor_size3.pkl", "wb")
pickle.dump(regressor2, outfile2)
pickle.dump(regressor3, outfile3)


inner_top=[11,15,19,21,272,273,275,285,286,341,342,4454,4495,4496]
outer_top=[23,24,25,256,277,281,289,4455,4456]
pants=[27,28,29,237,238,239,240,241,253,255,278,279,280,282,284,287,288,4458,4459]

intop_match = ["sleeveless top", "tunic", "sweater", "tshirt", "male shirt", "male sweater", "male tshirt", \
        "male track suit", "male sports shirt", "male shirt", "male polo", "male shirt", "sweatshirt", "sweater"]
outtop_match = ["jacket", "coat", "blazer", "track jacket", "male suit jacket", "male suit", "male track jacket",\
        "male formal jacket", "male jacket"]
pants_match = ["jeans", "pants", "shorts", "jeans", "jeans", "jeans", "jeans", "pants", "sweatpants", "shorts", \
        "male jeans", "male suit pants", "male knee-length shorts", "male swim shorts", "male sweatpants", "male track pants",
         "male sports shorts", "male pants", "male pants"]

def get_name(clothe_id):
    if clothe_id in inner_top:
        return intop_match[inner_top.index(clothe_id)]
    if clothe_id in outer_top:
        return outtop_match[outer_top.index(clothe_id)]
    if clothe_id in pants:
        return pants_match[pants.index(clothe_id)]
    return "None"




"""
for i in inner_top:
    for j in pants:
        ans = regressor2.predict([[i,j]])
        if ans == 0:
            print(i,j)

#print(regressor2.predict([[285, 279]]))
"""

