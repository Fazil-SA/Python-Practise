from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "welcome to my personal blog"

@app.route("/contact")
def contact():
    return "9745460637"

if(__name__=="__main__"):
    app.run(debug=True)
