from CryptoApp import app
from config import *
import datetime



from flask import render_template,request,redirect



@app.route("/")
def index():

    #here goes the acces to sqlite database#
    


    info =[
        {'date':'2024-02-11',
        'hour':'15:00',
        'coinFrom':'RON',
        'quantityFrom':'500',
        'coinTo':'EUR',
        'quantityTo':'99'},
        {'date':'2024-02-16',
        'hour':'07:30',
        'coinFrom':'EUR',
        'quantityFrom':'700',
        'coinTo':'BTC',
        'quantityTo':'21'},
        {'date':'2024-02-20',
        'hour':'10:45',
        'coinFrom':'BTC',
        'quantityFrom':'900',
        'coinTo':'ETH',
        'quantityTo':'35'}
    ]
    return render_template("index.html", inform = info, title = "Home" )
@app.route("/login")#, inside the () add -> methods=["GET","POST"])
def login():
    return render_template("login.html", title = "Log In")

@app.route("/purchase")#, inside the () add -> methods=["GET","POST"])
def purchase():
    #here goes an if where you say what POST does
    #inside this if goes another if with the date and time
    #
    return render_template ("purchase.html", title = "Purchase",)

@app.route("/status")
def status():
    #add an if 
    return render_template ("status.html", title = "Status")

@app.route("/logout")
def logout():
    return render_template("logout.html")