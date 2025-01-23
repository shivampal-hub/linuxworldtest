from flask import Flask
app = Flask(_name_)

@app.route("/info")
def lw():
    return "welcome to my webpage"
app.run(host='0.0.0.0',port=5000)
