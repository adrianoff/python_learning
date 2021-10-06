n = 1000

for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            for d in range(0, n):
                if a**3 + b ** 3 == c ** 3 + d ** 3:
                    print(a, b, c, d)
