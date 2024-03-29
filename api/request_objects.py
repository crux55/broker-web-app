from collections import namedtuple
from flask import request

TradeRequest = namedtuple('TradeRequest', 'symbol amount stop trailing')


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap


class Response:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
