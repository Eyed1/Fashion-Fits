import clothe_database as cd

cd.delete_clothes("./fashion.db")
cd.init_clothes("./fashion.db")

hoodie = cd.clothe('casual outer', 0, 255, 0, 20)
shirt = cd.clothe('casual inner', 0, 0, 255, 18)
pants = cd.clothe('casual pant', 25, 25, 25, 32)
nice_pants = cd.clothe('formal pant', 100, 100, 100, 30)
nice_shirt = cd.clothe('formal shirt', 0, 50, 150, 22)

cd.add_clothes('./fashion.db', hoodie)
cd.add_inventory('./fashion.db', [hoodie, shirt, pants])
cd.add_inventory('./fashion.db', [nice_pants, nice_shirt])

