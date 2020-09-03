import fxcmpy

class FXCMClient:

    def __init__(self):
        self.socket = fxcmpy.fxcmpy(config_file='config/fxcm.cfg', server='demo')

    def open_long(self, trade_request):
        self.close_shorts(trade_request)
        trade = self.socket.open_trade(symbol=trade_request.symbol, is_buy=True,
                                       is_in_pips=True,
                                       amount=trade_request.amount, time_in_force='GTC',
                                       order_type='AtMarket', stop=trade_request.stop,
                                       trailing_step=trade_request.trailing)
        print("Opening long: {}".format(trade))
        return trade

    def open_short(self, trade_request):
        self.close_longs(trade_request)
        trade = self.socket.open_trade(symbol=trade_request.symbol, is_buy=False,
                                       is_in_pips=True,
                                       amount=trade_request.amount, time_in_force='GTC',
                                       order_type='AtMarket', stop=trade_request.stop,
                                       trailing_step=trade_request.trailing)
        print("Opening short: {}".format(trade))
        return trade

    def close_longs(self, trade_request):
        positions = self.socket.get_open_positions()
        for i in range(len(positions)):
            if positions.currency[i] in [trade_request.symbol] and positions.isBuy[i]:
                trade = self.socket.close_trade(positions.tradeId[i], trade_request.amount, time_in_force='GTC',
                                                order_type='AtMarket')
                print("Closing long: {}".format(trade))

    def close_shorts(self, trade_request):
        positions = self.socket.get_open_positions()
        for i in range(len(positions)):
            if positions.currency[i] in [trade_request.symbol] and not positions.isBuy[i]:
                trade = self.socket.close_trade(positions.tradeId[i], trade_request.amount, time_in_force='GTC',
                                                order_type='AtMarket')
                print("Closing short: {}".format(trade))
