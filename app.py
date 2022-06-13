from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
<<<<<<< HEAD
    return render_template("WineQuality.html")
=======
    return "Machine Learning Application Started : Hello world"
>>>>>>> origin/main


if __name__ == "__main__":
    app.run(debug = True)
