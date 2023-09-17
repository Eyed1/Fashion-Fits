import csv
import json
import random

inner_top=[11,15,19,21,272,273,275,285,286,341,342,4454,4495,4496]
outer_top=[23,24,25,256,277,281,289,4455,4456]
pants=[27,28,29,237,238,239,240,241,253,255,278,279,280,282,284,287,288,4458,4459]

voredict = {}

def get_category_id(clothe_id):
    return voredict[str(clothe_id)]

def parse_data(combo):
    numinn = 0
    numout = 0
    numpant = 0
    fclothe = [0,0,0]
    for cd in combo:
        cd_id = get_category_id(cd["item_id"])
        if cd_id in inner_top:
            numinn+=1
            fclothe[0] = cd_id
        if cd_id in outer_top:
            numout+=1
            fclothe[1] = cd_id
        if cd_id in pants:
            numpant+=1
            fclothe[2] = cd_id
    if numinn == 1 and numpant == 1 and numout == 0:
        return [fclothe[0], fclothe[2]]
    if numinn == 1 and numpant == 1 and numout == 1:
        return fclothe
    return []

train_database = open("test.json", "r")
data = json.load(train_database)
outfile = open("train_data.jsonl", "w")
vore_combos = open("vore_data.json", "r")
vore_data = json.load(vore_combos)
print("stage 1 open files")

for key, value in vore_data.items():
    voredict[key] = int(value["category_id"])

assert(voredict["211990161"] == 15)

print("stage 1111 vore dict shit")



numsum2 = 0
numsum3 = 0
for comb in data:
    clothes = parse_data(comb["items"])
    if (len(clothes) == 0):
        continue
    datapoint = {"datapoint": clothes, "util": 1}
    json.dump(datapoint, outfile)
    outfile.write("\n")
    if len(clothes) == 2:
        numsum2 += 1
    if len(clothes) == 3:
        numsum3 += 1

print("stage 2 read through files")

for i in range(numsum2):
    top_id = random.randint(0, len(inner_top))
    pant_id = random.randint(0, len(pants))
    datapoint = {"datapoint": [top_id, pant_id], "util": 0}
    json.dump(datapoint, outfile)
    outfile.write("\n")

print("stage 3 random size 2")

for i in range(numsum3):
    intop_id = random.randint(0, len(inner_top))
    outtop_id = random.randint(0, len(outer_top))
    pant_id = random.randint(0, len(pants))
    datapoint = {"datapoint": [intop_id, outtop_id, pant_id], "util": 0}
    json.dump(datapoint, outfile)
    outfile.write("\n")

print("stage 4 random size 3")




