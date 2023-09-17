import clothe_database as cd
from PIL import Image
import urllib.request
cd.delete_clothes("./fashion.db")
cd.init_clothes("./fashion.db")

hoodie = cd.clothe(23, 0, 255, 0, 20)
shirt = cd.clothe(15, 0, 0, 255, 18)
pants = cd.clothe(27, 25, 25, 25, 32)
nice_pants = cd.clothe(255, 100, 100, 100, 30)
nice_shirt = cd.clothe(341, 0, 50, 150, 22)
tee_shirt = cd.clothe(342, 0, 200, 250, 20)

cd.add_clothes('./fashion.db', hoodie)
cd.add_inventory('./fashion.db',  [shirt, pants])
cd.add_inventory('./fashion.db', [nice_pants, nice_shirt])
cd.add_clothes('./fashion.db', tee_shirt)

#print(hoodie.category)

#print(cd.get_clothes('./fashion.db'))
#print(cd.get_category('./fashion.db', 'casual inner'))
#link = cd.get_id('./fashion.db', 5)[6]
#print(link)

#link, img = cd.get_img('./fashion.db', 5)
#img.show()
