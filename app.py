from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    """Display the home page."""
    
    return render_template(
        "index.html"
        )