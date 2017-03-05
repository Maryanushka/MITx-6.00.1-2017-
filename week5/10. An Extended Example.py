def genPrimes():
    x = 2
    p = []
    while True:
        for i in p:
            if x % i == 0:
                break
        else:
            yield x
            p.append(x)
        x += 1
