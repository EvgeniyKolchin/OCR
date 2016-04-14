from flask import Flask, url_for,  render_template, flash, redirect
from forms import LoginForm
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models

#@app.route("/")
#def hello():
    #return "Hello World!"

@app.route("/index")
def show_entries():
    return render_template('index.html')
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

if __name__ == "__main__":
    app.run(debug=True)