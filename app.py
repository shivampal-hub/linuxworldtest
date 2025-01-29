from flask import Flask
app = Flask(__name__)

@app.route("/info")
def lw():
    return "welcome to my newwebpage"
app.run(host='0.0.0.0',port=5000)
