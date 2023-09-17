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
    type varchar(255),\
    red INTEGER,\
    green INTEGER,\
    blue INTEGER,\
    length INTEGER,\
    image varchar(255)\
    )"
    run_cmd(db_path, cmd)

def delete_clothes(db_path):
    cmd = "DROP TABLE clothes"
    run_cmd(db_path, cmd)

class clothe:
    #category = "casual inner", "casual outer", "formal shirt", "formal pant", "casual pant"
    def __init__(self, category = "casual inner", r=0, g=0, b=0, length=0, image=""):
        self.category = category
        self.red = r
        self.green = g
        self.blue = b
        self.length = length
        self.image = image 

def add_clothes(db_path, clothes):
    cmd = f"INSERT INTO clothes (type, red, green, blue, length, image) VALUES (?, ?, ?, ?, ?, ?)"
    run_cmd(db_path, cmd, (clothes.category, clothes.red, clothes.green, clothes.blue, clothes.length, clothes.image,))

def add_inventory(db_path, inventory):
    for clothe in inventory:
        add_clothes(db_path, clothe)

def get_clothes(db_path):
    return run_cmd(db_path, "SELECT * FROM clothes")

def get_category(db_path, category):
    cmd = f"SELECT * FROM clothes WHERE clothes.type = ?"
    return run_cmd(db_path, cmd, (category,))

def get_id(db_path, num):
    cmd = f"SELECT * FROM clothes WHERE clothes.id = ?"
    res = run_cmd(db_path, cmd, (num,))
    if len(res) == 0:
        return None
    return res[0]

def get_img(db_path, num):
    cloth = get_id(db_path, num)
    link = cloth[6]
    urllib.request.urlretrieve(link, "img.png")
    img = Image.open("pant.png")
    return link, img

