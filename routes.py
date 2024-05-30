from flask import Blueprint, render_template

main = Blueprint("main",__name__)



@main.route("/")
def home():
   return render_template("login.html")

@main.route('/base')
def mostrar_productos():
    return render_template('base.html')
