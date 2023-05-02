from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="John")


@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name = username)

#for query parameters /profile?name=
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name)