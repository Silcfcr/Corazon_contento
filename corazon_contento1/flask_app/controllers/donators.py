from flask_app.models.user import User
from flask_app.models.donation import Donation
from flask_app import app
from flask import render_template, jsonify, request, redirect, session, flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route("/list_of_donators")
def list_of_donators():
    donators = User.get_all_donators()
    return render_template("list_of_donators.html", donators=donators)

@app.route("/register_as_donator")
def register_as_donator():
    return render_template("donator_registry.html")

@app.route("/make_donation")
def make_donation():
    return render_template("donation_registry.html")

@app.route("/register_donation", methods=['POST'])
def register_donation():
    data = {

    }
    id = Donation.new_donation(data)
    return redirect('/dashboard')






