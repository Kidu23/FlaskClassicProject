from CryptoApp import app

@app.route("/")
def hello():
    return "Hola esto es flask classic"