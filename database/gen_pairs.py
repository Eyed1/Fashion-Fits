import clothe_database as cd
import sqlite3

def gen_pairs(db_path, user = -1):
    clothesList = cd.get_clothes(db_path, user)
    print(db_path)
    print(len(clothesList))

#    print(len(clothesList))

    innerList=[]
    outerList=[]
    pantList=[]

    triple_list = [] #array of [inner, outer, pant]
    pair_list = [] #array of [inner, pant]

    for i in clothesList:
        if i[2]=="casual inner" or i[2]=="formal shirt":
            innerList.append(i)
        elif i[2]=="casual outer":
            outerList.append(i)
        else: #"formal pant", "casual pant"
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
