from flask import (Flask, render_template, redirect, url_for)
app = Flask(__name__)

### redirect to login page
@app.route("/")
##def home():
##    return render_template()

@app.route("/login")
def login():
    return render_template("login.html")




















### loops the code- has to be at the bottom.
if __name__== "__main__":
#   with app.app_context():
 #       db.create_all()
    app.run(debug=True)