import clothe_database as cd
import gen_pairs as gp
import sqlite3

listL=[cd.clothe("casual inner",0,0,0,0),cd.clothe("casual inner",1,1,1,1),cd.clothe("casual inner",2,2,2,2),
       cd.clothe("casual outer",0,0,0,0),cd.clothe("casual outer",1,1,1,1),
       cd.clothe("formal shirt",0,0,0,0),cd.clothe("formal shirt",1,1,1,1),
       cd.clothe("formal pant",0,0,0,0),cd.clothe("formal pant",1,1,1,1),
       cd.clothe("casual pant",0,0,0,0),cd.clothe("casual pant",1,1,1,1)]

cd.delete_clothes("./fashion.db")
cd.init_clothes("./fashion.db")

for i in listL:
    cd.add_clothes("./fashion.db",i)
gp.gen_pairs("./fashion.db")
