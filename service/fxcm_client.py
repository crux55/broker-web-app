import fxcmpy

class FXCMClient:

    def __init__(self):
        self.socket = fxcmpy.fxcmpy(config_file='config/fxcm.cfg', server='demo')

    def open_long(self, symbol, amount):
        self.close_shorts(symbol, amount)
        trade = self.socket.open_trade(symbol=symbol, is_buy=True,
                                       is_in_pips=True,
                                       amount=amount, time_in_force='GTC',
                                       order_type='AtMarket')
        print("Opening long: {}".format(trade))
        return trade

    def open_short(self, symbol, amount):
        self.close_longs(symbol, amount)
        trade = self.socket.open_trade(symbol=symbol, is_buy=False,
                                       is_in_pips=True,
                                       amount=amount, time_in_force='GTC',
                                       order_type='AtMarket')
        print("Opening short: {}".format(trade))
        return trade

    def close_longs(self, symbol, amount):
        positions = self.socket.get_open_positions()
        for i in range(len(positions)):
            if positions.currency[i] in [symbol] and positions.isBuy[i]:
                trade = self.socket.close_trade(positions.tradeId[i], amount, time_in_force='GTC',
                                   order_type='AtMarket')
                print("Closing long: {}".format(trade))

    def close_shorts(self, symbol, amount):
        positions = self.socket.get_open_positions()
        for i in range(len(positions)):
            if positions.currency[i] in [symbol] and not positions.isBuy[i]:
                trade = self.socket.close_trade(positions.tradeId[i], amount, time_in_force='GTC',
                                        order_type='AtMarket')
                print("Closing short: {}".format(trade))
