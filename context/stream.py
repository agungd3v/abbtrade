import time, json
from binance import ThreadedWebsocketManager
from context.useenv import api_key, api_secret

def stream(pair, callback):
    data_on_stream = []
    twm = ThreadedWebsocketManager(api_key = api_key, api_secret = api_secret)
    twm.start()

    def handle_message(msg):
        result_formatter = json.dumps(msg)
        as_result = json.loads(result_formatter)

        data_formatter = {
            "price": format(float(as_result["data"]["p"]), ".2f"),
            "quantity": format(float(as_result["data"]["q"]), ".4f"),
            "action": "BUY" if as_result["data"]["m"] else "SELL" 
        }
        data_on_stream.insert(0, data_formatter)

        if len(data_on_stream) >= 5:
            twm.stop()
            callback(data_on_stream)

    streams = [pair]
    twm.start_multiplex_socket(callback = handle_message, streams = streams)
    twm.join()