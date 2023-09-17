from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
import sys
sys.path.append("../backend")
import user 
import get_name
sys.path.append("../database")
import clothe_database as cd

app = Flask(__name__)
Cors = CORS(app)


def hex_to_rgb(hex_color):
    # Remove the '#' character if it exists
    hex_color = hex_color.lstrip('#')
    
    # Check if the hex_color is a valid hexadecimal color code
    if not all(c in '0123456789ABCDEFabcdef' for c in hex_color) or len(hex_color) != 6:
        raise ValueError("Invalid hexadecimal color code")
    
    # Convert the hexadecimal color code to decimal values
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    return r, g, b


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/wardrope", methods=["POST"])
def addClothe():
    if request.method == "POST":
        clothes = request.get_json()
        color = clothes.get("color")
        ttype = clothes.get("type")
        cat = clothes.get("cat")
        id_val = get_name.get_id(ttype)
        r,g,b = hex_to_rgb(color)
        cloth = cd.clothe(id_val, r, g, b)
        user.add_clothes(cloth, -1)

@app.route("/api/wardrope/fits", methods=["GET"])
def getFits():
    a, b = user.get_clothes(-1, "hot")
    return jsonify(a), jsonify(b)

@app.route("/api/wardrope", methods=["GET"])
def getWardrope():
    return user.get_clothes(-1)

if __name__ == '__main__':
    app.run(port=1934, debug=True)
