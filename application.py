from flask import Flask, render_template, request
import os
from crearlista import crearlista

documentos = os.environ['USERPROFILE'] + "\\Documents\\"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        if(request.form["archivo_entrada"] != ""):
            arch_entrada = documentos + request.form["archivo_entrada"]
            mensaje = crearlista(arch_entrada)
            return render_template("index.html", mensaje = mensaje)
    else:
        mensaje = ""
        return render_template("index.html")
