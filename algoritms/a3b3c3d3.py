n = 100

for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            h = a**3 + b ** 3 - c ** 3
            if h < 0:
                break
            d = int(round(h ** (1/3)))
            if d > n:
                break
            if a**3 + b ** 3 == c ** 3 + d ** 3 and a+b != c+d:
                print(a, b, c, d)
                break
