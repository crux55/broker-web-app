from flask import Flask
from api.request_objects import TradeRequest, convert_input_to
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


@app.route("/objecttest", methods=['POST'], endpoint='simple_objtest')
@convert_input_to(TradeRequest)
def obj_test(traderequest):
    print(traderequest)
    return "", 200


@app.route("/buy", methods=['POST'], endpoint='simple_buy')
@convert_input_to(TradeRequest)
def simple_buy(trade_request):
    print("==================")
    print("  Long requested")
    print("==================")
    fxcm_client.open_long(trade_request)
    return "Longed: {}".format(trade_request.symbol), 200


@app.route("/sell", methods=['POST'], endpoint='simple_sell')
@convert_input_to(TradeRequest)
def simple_sell(trade_request):
    print("==================")
    print(" Short requested")
    print("==================")
    fxcm_client.open_short(trade_request)
    return "Shorted: {}".format(trade_request.symbol), 200


if __name__ == "__main__":
    print('Starting web app')
    app.run(host='0.0.0.0', port=8080)
