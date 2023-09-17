from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
import sys
sys.path.append(../backend)
import user 
sys.path.append(../database)
import clothe_database as cd

app = Flask(__name__)
Cors = CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_clothes", methods=["POST"])
def add_clothes():
    if request.method == "POST":
        clothes = request.get_json()
        cloth = cd.clothes(clothes.get('category'), clothes.get('red'), clothes.get('green'),\
                clothes.get('blue'))
        user.add_clothes(cloth, -1)

        

if __name__ == '__main__':
    app.run(port=1934, debug=True)
