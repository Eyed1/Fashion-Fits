import clothe_database as cd
import gen_pairs as gp
import hard_code as hcm
import sqlite3

listL=[cd.clothe("casual outer",186,13,23,0),cd.clothe("casual outer",47,47,47,0),cd.clothe("casual inner",28,28,28,0),
       cd.clothe("casual inner",144,187,230,0),cd.clothe("casual inner",58,19,62,0),cd.clothe("formal shirt",109,120,174),
       cd.clothe("casual inner",160,253,120,0),cd.clothe("casual pant",59,89,115,0),cd.clothe("casual pant",143,144,113,0),
       cd.clothe("casual pant",27,21,25,0),cd.clothe("formal pant",33,38,58,0),cd.clothe("casual pant",198,1,18,0)]

cd.delete_clothes("./fashion.db")
cd.init_clothes("./fashion.db")

for i in listL:
    cd.add_clothes("./fashion.db",i)

trips, pairs=gp.gen_pairs("./fashion.db")

cd.get_clothes("./fashion.db")

list=[]

for i in pairs:
    if(hcm.find_match_pair(i[0],i[1])):
        list.append(i);
for i in trips:
    if(hcm.find_match_triple(i[0],i[1],i[2])):
        list.append(i);

for i in range(len(list)):
    print(list[i])
