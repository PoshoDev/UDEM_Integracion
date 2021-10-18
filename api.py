from flask import *
import json, time
import database as db
import api, back

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    data = {
        "Page":"Home",
        "Message":"Estas en la pagina principal! Lee nuestra documentacion para saber como generar un request. :)"
        }
    return json.dumps(data)

# /user/?user=USERNAME
@app.route("/user/", methods=["GET"])
def request_user():
    query = str(request.args.get("user"))
    data = {
        "Page":"Request:User",
        "Message":f"Attempting to fetch from user: {query}"
        }
    return json.dumps(data)

# /inventario/?marca=USERNAME
@app.route("/inventario/", methods=["GET"])
def request_inventario():
    marca = str(request.args.get("marca"))

    if marca == "None": q = db.Call("AutomovilGetAll")
    else: q = db.Call("AutomovilGetMarca", marca)
    l = []
    for i in q:
        l.append({"id":i[0],"modelo":i[1],"color":i[2],"precio":i[3],"unidades":i[4]})
    data = "{"
    for i in range(len(l)):
        data += f"'{i}':{l[i]},"
    data += "}"
    return data


if __name__ == "__main__":
    app.run(port=6969)
