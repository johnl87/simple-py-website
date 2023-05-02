from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="John")


@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name = username)