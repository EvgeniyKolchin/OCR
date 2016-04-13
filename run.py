from flask import Flask, url_for,  render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ad")
def show_entries():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(debug=True)