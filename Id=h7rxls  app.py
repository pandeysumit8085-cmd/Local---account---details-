import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    with open("data.txt", "a") as f:
        f.write(f"{name}, {email}\n")

    return "Form Submitted Successfully!"

port = int(os.environ.get("PORT", 10000))
app.run(host='0.0.0.0', port=port)
