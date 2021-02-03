import fxcmpy

class FXCMClient:

    def __init__(self):
        self.socket = fxcmpy.fxcmpy(config_file='config/fxcm.cfg', server='demo')

    def open_long(self, trade_request):
        if trade_request.flipping:
            print("Flipping longs")
            self.close_shorts(trade_request)
        if not trade_request.allow_multi and self.get_open_longs(trade_request.symbol):
            print("Not allowing multis and we're in a long position already")
            return

        trade = self.socket.open_trade(symbol=trade_request.symbol, is_buy=True,
                                       is_in_pips=True,
                                       amount=trade_request.amount, time_in_force='GTC',
                                       order_type='AtMarket',
                                       limit=trade_request.limit,
                                       stop=trade_request.stop,
                                       trailing_step=float(trade_request.trailing))
        print("Opening long: {}".format(trade))
        return trade

    def open_short(self, trade_request):
        if trade_request.flipping:
            print("Flipping shorts")
            self.close_longs(trade_request)
        if not trade_request.allow_multi and self.get_open_shorts(trade_request.symbol):
            print("Not allowing multis and we're in a short position already")
            return
        trade = self.socket.open_trade(symbol=trade_request.symbol, is_buy=False,
                                       is_in_pips=True,
                                       amount=trade_request.amount, time_in_force='GTC',
                                       order_type='AtMarket',
                                       limit=trade_request.limit,
                                       stop=trade_request.stop,
                                       trailing_step=float(trade_request.trailing))
        print("Opening short: {}".format(trade))
        return trade

    def get_open_longs(self, symbol):
        positions = self.socket.get_open_positions()
        ids = []
        for i in range(len(positions)):
            if positions.currency[i] in [symbol] and positions.isBuy[i]:
                ids.append(positions.tradeId[i])
        return ids

    def get_open_shorts(self, symbol):
        positions = self.socket.get_open_positions()
        ids = []
        for i in range(len(positions)):
            if positions.currency[i] in [symbol] and not positions.isBuy[i]:
                ids.append(positions.tradeId[i])
        return ids

    def close_longs(self, trade_request):
        print("Closing longs")
        ids = self.get_open_longs(trade_request.symbol)
        print("{} long ids found".format(len(ids)))
        for i in range(len(ids)):
            trade = self.socket.close_trade(ids[i], trade_request.amount, time_in_force='GTC',
                                            order_type='AtMarket')
            print("Closing long: {}".format(trade))

    def close_shorts(self, trade_request):
        print("Closing shorts")
        ids = self.get_open_shorts(trade_request.symbol)
        print("{} short ids found".format(len(ids)))
        for i in range(len(ids)):
            trade = self.socket.close_trade(ids[i], trade_request.amount, time_in_force='GTC',
                                            order_type='AtMarket')
            print("Closing short: {}".format(trade))

    def trade_to_object(self, trade):
        new_trade = {}
        for param in trade.parameter:
            new_trade[param] = trade.__getattr(param)

    def close_id(self, id, amount):
        return self.socket.close_trade(id, amount=amount)

    def close_all(self):
        return self.socket.close_all()