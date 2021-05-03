from flask import Flask, request
from api.request_objects import TradeRequest, convert_input_to
from service.fxcm_client import FXCMClient


app = Flask(__name__)
print('Starting client...')
fxcm_client = FXCMClient()
print('Client started')

def reqursive_to_json(obj):
    _json = {}

    if isinstance(obj, tuple):
        datas = obj._asdict()
        for data in datas:
            if isinstance(datas[data], tuple):
                _json[data] = (reqursive_to_json(datas[data]))
            else:
                print(datas[data])
            _json[data] = (datas[data])
    return _json


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
    return reqursive_to_json(traderequest), 200


@app.route("/buy", methods=['POST'], endpoint='simple_buy')
@convert_input_to(TradeRequest)
def simple_buy(trade_request):
    print("==================")
    print("  Long requested")
    print("==================")
    trade = fxcm_client.open_long(trade_request)
    return str(trade.get_tradeId()), 200


@app.route("/sell", methods=['POST'], endpoint='simple_sell')
@convert_input_to(TradeRequest)
def simple_sell(trade_request):
    print("==================")
    print(" Short requested")
    print("==================")
    trade = fxcm_client.open_short(trade_request)
    return str(trade.get_tradeId()), 200

@app.route("/close", methods=['GET'], endpoint='simple_close')
def simple_close():
    id = request.args.get('id')
    amount = request.args.get('amount')
    fxcm_client.close_id(id, amount)
    return "", 200

@app.route("/closeall", methods=['GET'], endpoint='close_all')
def simple_close():
    fxcm_client.close_all()
    return "", 200

@app.route("/dump", methods=['POST'], endpoint='dump')
def dump():
    print("test")
    print(request.get_json())
    # logging.info("test")
    # logging.info(request.get_json())
    return "", 200


if __name__ == "__main__":
    print('Starting web app')
    app.run(host='0.0.0.0', port=8080)
