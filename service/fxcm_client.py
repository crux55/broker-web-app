import fxcmpy

class FXCMClient:

    def __init__(self):
        self.socket = fxcmpy.fxcmpy(config_file='config/fxcm.cfg', server='demo', log_level='debug', log_file="fxcm.log")

    def create_entry(self, symbol, amount, limit, stop):
        trade = self.socket.open_trade(symbol=symbol, is_buy=True,
                                       is_in_pips=True,
                                       amount=amount, time_in_force='GTC',
                                       order_type='AtMarket', limit=limit)
        print(trade)
        return trade

    def close(self, symbol):
        for_symbol = self.socket.close_all_for_symbol(symbol)
        print(for_symbol)
        return for_symbol
