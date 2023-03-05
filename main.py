from context.stream import stream

def main_callback(cb):
    print(cb)

def main():
    return stream("btcusdt@aggTrade", main_callback)

if __name__ == "__main__":
    main()