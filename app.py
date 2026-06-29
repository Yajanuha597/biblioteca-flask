from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista donde se guardarán las tareas
tareas = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":
        tarea = request.form["tarea"]
        tareas.append(tarea)
        return redirect("/lista")

    return render_template("agregar.html")

@app.route("/lista")
def lista():
    return render_template("lista.html", tareas=tareas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)