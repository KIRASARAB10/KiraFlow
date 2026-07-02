from flask import Flask, render_template

from helpers import login_required

# Configure application
app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Display the home page."""
    return render_template("index.html")
    
    

@app.route("/register", methods=["POST", "GET"])
def register():
    """Display the registration page."""

    return
    

@app.route("/login")
def login():
    """Display the login page."""
    
    return