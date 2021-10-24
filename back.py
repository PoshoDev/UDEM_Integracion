from flask import *
import loaf

app = Flask(__name__, template_folder="Front\\templates", static_folder="Front\\templates\\static")

loaf.bake(host='192.168.1.241', port=3306, db="autos")

@app.route("/")
def home():
    return render_template("testicle.html")

@app.route("/catalogo")
def catalogo():
    colores = loaf.query("SELECT color FROM automovil")
    print(colores)
    return render_template("catalogo.html", lol=colores)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/send_form", methods=["POST"])
def send_form():
    nom = request.form.get("nombre")
    sem = request.form.get("semestre")
    pas = request.form.get("pasatiempo")
    print(nom)
    print(sem)
    print(pas)
    return redirect(url_for("catalogo"))

if __name__ == "__main__":
    app.run(port=4420)
