from flask import Flask, redirect, request,url_for
import sqlite3

app = Flask(__name__)
@app.route("/success/<name>", methods=['GET'])
def success(name):
    return "Welcome Back %s"% name
@app.route("/failed/<name>", methods=['GET'])
def failed(name):
    return "Login Failed %s Please Try Again"% name
@app.route("/login", methods=['POST'])
def login():
    if request.methods== 'POST' :
        username= request.form['username']
        password= request.form['password']
        if userLogin(username,password):
            return redirect(url_for("success", name=username))
        else:
            return redirect(url_for("failed", name=username))
        
def userLogin(username,password):
    connection=sqlite3.connect('user.db')
    cursor=connection.cursor()
    cursor.execute("SELECT username, password FROM user WHERE username =? and password=?", (username,password))
    count=cursor.fetchone()
    connection.close()
    return count

if __name__ == '__main__':
    print("This is Flask Program")
    app.run()