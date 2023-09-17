import sqlite3
from PIL import Image
import urllib.request

def run_cmd(db_path, command, params = ()):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(command, params)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def init_clothes(db_path):
    cmd = "CREATE TABLE IF NOT EXISTS clothes(\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    user USER,\
    type INTEGER,\
    red INTEGER,\
    green INTEGER,\
    blue INTEGER,\
    length INTEGER,\
    image varchar(255),\
    name varcharr(255)\
    )"
    run_cmd(db_path, cmd)

def delete_clothes(db_path):
    cmd = "DROP TABLE clothes"
    run_cmd(db_path, cmd)

class clothe:
    #category = "casual inner", "casual outer", "formal shirt", "formal pant", "casual pant"
    def __init__(self, category = "casual inner", r=0, g=0, b=0, length=0, image="", name = ""):
        self.category = category
        self.red = r
        self.green = g
        self.blue = b
        self.length = length
        self.image = image 
        self.name = name

def add_clothes(db_path, clothes, user = -1):
    cmd = f"INSERT INTO clothes (user, type, red, green, blue, length, image, name) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    run_cmd(db_path, cmd, (user, clothes.category, clothes.red, clothes.green, clothes.blue, clothes.length, clothes.image, clothes.name))

def add_inventory(db_path, inventory, user = -1):
    for clothe in inventory:
        add_clothes(db_path, clothe, user)

#Get clothes of one user
def get_clothes(db_path, user = -1):
    return run_cmd(db_path, "SELECT * FROM clothes WHERE clothes.user = ?", (user,))

#Get clothes of a certain type of a category
def get_category(db_path, category, user=-1):
    cmd = f"SELECT * FROM clothes WHERE clothes.type = ? AND clothes.user = ?"
    return run_cmd(db_path, cmd, (category, user,))

#Get clothe given id
def get_id(db_path, num):
    res = run_cmd(db_path, "SELECT * FROM clothes WHERE clothes.id = ?", (num,))
    if len(res) == 0:
        return None
    return res[0]

#get image. Run img.show() to show image.
def get_img(db_path, num):
    cloth = get_id(db_path, num)
    link = cloth[7]
    urllib.request.urlretrieve(link, "img.png")
    img = Image.open("img.png")
    return link, img

