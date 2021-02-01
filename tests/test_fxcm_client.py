from unittest import TestCase
from unittest.mock import Mock

from api.request_objects import TradeRequest
from service.fxcm_client import FXCMClient


class TestFXCMClient(TestCase):
    def test_open_long(self):
        sc = Mock()
        fxcm_client = FXCMClient(False)
        sc.get_open_positions.return_value = []
        sc.open_trade.return_value = "Yes"
        fxcm_client.socket = sc
        trade = fxcm_client.open_long(TradeRequest(symbol="AUD/JPY", amount=80, stop=0,
                                                   trailing=0, flipping=False, allow_multi=False))
        print(trade)
