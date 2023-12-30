from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods=["GET"])
def home_route():
    return render_template("home.html")

@app.route("/edit-home", methods=["POST"])
def edit_home():
    return "<h2> it works </h2>"

if __name__ ==  "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
