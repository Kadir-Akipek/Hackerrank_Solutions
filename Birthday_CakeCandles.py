def birthdayCakeCandles(candles):
    tallcandle = 0
    x = max(candles)
    for i in candles:
        if i == x:
            tallcandle += 1
    return tallcandle