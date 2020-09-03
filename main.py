from flask import Flask, request
from service.fxcm_client import FXCMClient


app = Flask(__name__)
print('Starting client...')
fxcm_client = FXCMClient()
print('Client started')


@app.route("/")
def test_endpoint():
    return "Server is up"


@app.route("/errortest")
def error_test():
    return "Error", 400


@app.route("/buy", methods=['POST'])
def simple_buy():
    symbol = request.json['symbol']
    stop = None
    trailing = None
    try:
        stop = request.json['stop']
    except KeyError:
        pass
    try:
        trailing = request.json['trailing']
    except KeyError:
        pass
    fxcm_client.open_long(symbol, request.json['amount'], stop, trailing)
    return "Longed: {}".format(symbol), 200


@app.route("/sell", methods=['POST'])
def simple_sell():
    symbol = request.json['symbol']
    stop = None
    trailing = None
    try:
        stop = request.json['stop']
    except KeyError:
        pass
    try:
        trailing = request.json['trailing']
    except KeyError:
        pass
    fxcm_client.open_short(symbol, request.json['amount'], stop, trailing)
    return "Shorted: {}".format(symbol), 200


if __name__ == "__main__":        # on running python main.py
    print('Starting web app')
    app.run(host='0.0.0.0', port=8080)                     # run the flask app
