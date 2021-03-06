from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/dojos')
def schools():
    friends = Dojo.get_all()
    return render_template('dojos.html', all_dojos = friends)
@app.route('/create_dojo', methods = ['POST'])
def create():
    data = {
        'name': request.form["nname"]
    }
    print(data)
    friends = Dojo.save(data)
    return redirect('/dojos')
@app.route('/dojos/<int:num>/<x>')
def show(num,x):
    friends = Ninja.get_dojos(num)
    session['x'] = x
    return render_template('show.html', num = num, all_nijas = friends, x = session['x'])

@app.route('/ninja')
def ninja():
    friends = Ninja.get_all()
    places = Dojo.get_all()
    return render_template("ninjas.html",all_ninjas = friends, all_dojos = places)
@app.route('/add_ninja', methods=['POST'])
def set_ninja():
    if not Dojo.validate_ninja(request.form):
        return redirect('/ninja')
    data = {
        'dojo_id':request.form['dojo_id'],
        'fname':request.form['fname'],
        'lname':request.form['lname'],
    }
    friends = Ninja.add_to_dojo(data)
    return redirect('/ninja')