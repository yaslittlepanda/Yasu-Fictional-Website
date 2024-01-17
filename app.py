from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
    name = request.args.get("name")
    email = request.args.get("email")
    print(name)
    props = {
        "name": name,
        "email": email
    }
    return render_template("confirmation.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)