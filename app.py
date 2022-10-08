#flask boiler
from flask import Flask, render_template

from datetime import datetime


# to facilitate db manipulation via py
#from flask_sqlalchemy import SQLAlchemy
#import mysql.connector as con

#mydb = con.connect(host="localhost", user="root", password="As$2652000")
#cursor = mydb.cursor()
#cursor.execute("show databases")
#print(cursor.fetchall())


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@server/db"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#class ShopShop(db.Model):

#   login_id = db.Column(db.String(100), nullable=False)
#    pw = db.Column(db.String(100), nullable=False)
#    login_span = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def main_pg():
    return render_template('main.pg.html')

@app.route("/")
def auth():
    return render_template('authorization.pg.html')

@app.route("/")
def checkout():
    return render_template('checkout.html')

@app.route("/")
def forgot_pw():
    return render_template('forgot.pw.html')

@app.route("/")
def forgot_pw2():
    return render_template('forgot.pw(2).html')

@app.route("/")
def contact():
    return render_template('contact.html')

@app.route("/")
def pg_when():
    return render_template('pg.when.signed.in.html')



#making the app run
if __name__ == "__main__":
    app.run(debug=True, port =8000) # debug mode enable necessary