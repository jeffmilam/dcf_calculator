from flask import Flask, render_template, jsonify, request



app = Flask(__name__, template_folder='www/templates', static_folder='www/assets')

@app.route("/")
def index():
    return render_template("formula.html", msg="Hello world")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
