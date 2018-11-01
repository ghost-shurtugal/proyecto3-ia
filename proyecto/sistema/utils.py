def getInteger(msg,
               error="Lo que escribió no es un número, inténtelo otra vez"):
    while True:
        try:
            return int(input(msg))
        except Exception:
            print(error)


def getIntegerFromInterval(msg, fromN, toN, error):
    while True:
        result = getInteger(msg)
        if result >= fromN and result <= toN:
            return result
        print(error)
