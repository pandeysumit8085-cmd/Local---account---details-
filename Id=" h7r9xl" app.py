from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    with open("data.txt", "a") as f:
        f.write(f"{name}, {email}\n")

    return "Form Submitted Successfully!"

app.run(host='0.0.0.0', port=5000)
