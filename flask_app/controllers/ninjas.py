from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/dojos')
def schools():
    friends= Dojo.get_all()
    return render_template('dojos.html', all_dojos = friends)
@app.route('/create_dojo', methods = ['POST'])
def create():
    data = {
        'name': request.form["nname"]
    }
    print(data)
    friends = Dojo.save(data)
    return redirect('/dojos')