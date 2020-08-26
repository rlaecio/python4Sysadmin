#!/usr/bin/env python3

from flask import Flask
import json


app = Flask(__name__)

@app.route("")
def index():
    retorno = {
        "app" : "Sistema de mensagens",
        "version":
    }


if __name__ == "__main__":
    app.run(debug=True)