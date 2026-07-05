from flask import Flask, render_template
from flask_session import Session

from helpers import login_required
from models import db

# Create the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///KiraFlow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Store sessions on the server
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Secret key used to sign session data
app.config["SECRET_KEY"] = "dev-secret-key"


@app.after_request
def after_request(response):
    """Ensure responses aren't cached."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Display the home page."""
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    pass


@app.route("/login", methods=["GET", "POST"])
def login():
    """Authenticate a user."""
    pass