import imp
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def schools():
    return render_template('dojos.html')