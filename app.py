from flask import Flask, request, jsonify

app = Flask(__name__)             # create an app instance
from service.fxcm_client import FXCMClient

print('Starting client...')
fxcm_client = FXCMClient()
print('Client started')

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"


@app.route("/errortest")
def errortest():
    return "Error", 400


@app.route("/buy", methods=['POST'])
def simple_buy():
    print(request.json['symbol'],
          request.json['amount'],
          request.json['limit'],
          request.json['stop'])
    entry = fxcm_client.create_entry(request.json['symbol'], request.json['amount'], request.json['limit'],
                                     request.json['stop'])
    return "Good", 200

@app.route("/sell", methods=['POST'])
def simple_sell():
    return jsonify(fxcm_client.close(request.json['symbol']))

if __name__ == "__main__":        # on running python app.py
    print('Starting web app')
    app.run(host='0.0.0.0')                     # run the flask app
