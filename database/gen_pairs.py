import clothe_database as cd
import sqlite3

inner_top=[11,15,19,21,272,273,275,285,286,341,342,4454,4495,4496]
outer_top=[23,24,25,256,277,281,289,4455,4456]
pants=[27,28,29,237,238,239,240,241,253,255,278,279,280,282,284,287,288,4458,4459]

def gen_pairs(db_path, user = -1):
    clothesList = cd.get_clothes(db_path, user)
    #print(db_path)
    #print(len(clothesList))

#    print(len(clothesList))

    innerList=[]
    outerList=[]
    pantList=[]

    triple_list = [] #array of [inner, outer, pant]
    pair_list = [] #array of [inner, pant]

    for i in clothesList:
        if i[2] in inner_top:
            innerList.append(i)
        elif i[2] in outer_top:
            outerList.append(i)
        elif i[2] in pants: #"formal pant", "casual pant"
            pantList.append(i)

    #print(len(innerList))

    for i in innerList:
        for j in outerList:
            for k in pantList:
              triple_list.append([i, j, k])


    for i in innerList:
        for j in pantList:
            pair_list.append([i, j])
            
    return triple_list, pair_list
