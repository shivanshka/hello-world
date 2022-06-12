from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return "Machine Learning Application Started : Hello world ????"


if __name__ == "__main__":
    app.run(debug = True)
