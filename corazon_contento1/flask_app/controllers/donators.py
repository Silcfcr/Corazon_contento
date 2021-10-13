from flask_app.models.user import User
from flask_app.models.donation import Donation
from flask_app import app
from flask import render_template, jsonify, request, redirect, session, flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route("/list_of_donators")
def list_of_donators():
    donators = User.get_all_donators()
    if "user_id" in session:
        data = {
            "id" : session['user_id']
        }
        user = User.get_one_user_by_id(data)
        return render_template("list_of_donators.html", donators=donators, user=user)
    user = False
    print("Hello", user)
    return render_template("list_of_donators.html", donators=donators, user=user)

@app.route("/register_as_donator")
def register_as_donator():
    return render_template("donator_registry.html")

@app.route("/make_donation")
def make_donation():
    data = {
        "id" : session['user_id']
    }
    user = User.get_one_user_by_id(data)
    print(user)
    return render_template("donation_registry.html", user = user)

@app.route("/register_donation", methods=['POST'])
def register_donation():
    print(request.form)
    data = {
        'type' : request.form['type'],
        'transport' : request.form['transport'],
        'portions' : request.form['portions'],
        'expiration': request.form['expiration'],
        'description' : request.form['description'],
        'status' : request.form['status'],
        'donator_id': request.form['donator_id'],
        'receiver_id' : request.form['receiver_id']
    }
    id = Donation.register_new_donation(data)
    return redirect('/dashboard')

@app.route("/list_of_donations")
def list_of_available_donations():
    donations = Donation.get_all_available_donations()
    return render_template("list_of_donations.html", donations=donations)

@app.route("/see_donation/<int:id>")
def show_donation(id):
    data = {
        'id' : id
    }
    donation = Donation.get_one_donation_by_id_with_details(data)
    print(donation)
    return render_template("show_donation.html", donation=donation)

@app.route("/claim_donation/<int:id>")
def claim_donation(id):
    data = {
        'id' : id,
        'status' : "solicitada",
        'receiver_id' : session['user_id']
    }
    donation = Donation.change_donation_status(data)
    print(donation)
    print("Yes!")
    return redirect('/dashboard')


