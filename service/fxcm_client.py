import fxcmpy

class FXCMClient:

    def __init__(self):
        self.socket = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')

    def create_entry(self, symbol, amount, limit, stop):
        self.socket.open_trade(symbol=symbol, is_buy=True, is_in_pips=False, amount=amount, time_in_force='GTC',
                               order_type='AtMarket', limit=limit, stop=stop)

    def close(self, symbol):
        self.socket.close_all_for_symbol(symbol)
