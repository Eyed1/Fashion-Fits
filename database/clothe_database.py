import sqlite3

def run_cmd(command, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()
    cursor.close()
    conn.close()


def init_clothes(db_path):
    cmd = "CREATE TABLE IF NOT EXISTS clothes(\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    type varchar(255),\
    red INTEGER,\
    green INTEGER,\
    blue INTEGER,\
    length INTEGER\
    )"
    run_cmd(cmd, db_path)

def delete_clothes(db_path):
    cmd = "DROP TABLE clothes"
    run_cmd(cmd, db_path)

class clothe:
    #category = "casual inner", "casual outer", "formal shirt", "formal pant", "casual pant"
    def __init__(self, category = "casual inner", r=0, g=0, b=0, length=0):
        self.category = category
        self.red = r
        self.green = g
        self.blue = b
        self.length = length

def add_clothes(db_path, clothe):
    cmd = f"INSERT INTO clothes (type, red, green, blue, length)\
            VALUES ({clothe.category}, ?, ?, ?, ?)"


