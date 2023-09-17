import clothe_database as cd
from PIL import Image
import urllib.request
cd.delete_clothes("./fashion.db")
cd.init_clothes("./fashion.db")

hoodie = cd.clothe('casual outer', 0, 255, 0, 20)
shirt = cd.clothe('casual inner', 0, 0, 255, 18)
pants = cd.clothe('casual pant', 25, 25, 25, 32)
nice_pants = cd.clothe('formal pant', 100, 100, 100, 30)
nice_shirt = cd.clothe('formal shirt', 0, 50, 150, 22)
tee_shirt = cd.clothe('casual inner', 0, 200, 250, 20)

cd.add_clothes('./fashion.db', hoodie)
cd.add_inventory('./fashion.db', [hoodie, shirt, pants])
cd.add_inventory('./fashion.db', [nice_pants, nice_shirt])
cd.add_clothes('./fashion.db', tee_shirt)

#print(cd.get_clothes('./fashion.db'))
#print(cd.get_category('./fashion.db', 'casual inner'))
#link = cd.get_id('./fashion.db', 5)[6]
#print(link)

#link, img = cd.get_img('./fashion.db', 5)
#img.show()
