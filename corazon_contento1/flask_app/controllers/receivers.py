from flask_app.models.user import User
from flask_app import app
from flask import render_template,request, redirect, session, flash

@app.route("/list_of_receivers")
def list_of_receivers():
    receivers =User.get_all_receivers()
    if "user_id" in session:
        data = {
            "id" : session['user_id']
        }
        user = User.get_one_user_by_id(data)
        return render_template("list_of_receivers.html", receivers=receivers, user=user)
    user = False
    return render_template("list_of_receivers.html", receivers=receivers, user=user)

@app.route("/register_as_receiver")
def register_as_receiver():
    return render_template("receiver_registry.html")



