import clothe_database as cd
import sqlite3

def gen_pairs(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clothes")
    clothesList = cursor.fetchall()

    print(len(clothesList))

    innerList=[]
    outerList=[]
    pantList=[]

    for i in clothesList:
        if i[1]=="casual inner" or i[1]=="formal shirt":
            innerList.append(i)
        elif i[1]=="casual outer":
            outerList.append(i)
        else: #"formal pant", "casual pant"
            pantList.append(i)

    #print(len(innerList))

    for i in innerList:
        for j in outerList:
            for k in pantList:
                cmd = f"INSERT INTO clothe_pairs (inner, outer, pant)\
                        VALUES ({i},{j},{k})"
                print([i[0],j[0],k[0]])
