for i in range(452021, 453000):
    k = 0
    mi = 100000
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            if j < mi: mi = j
    k = i / mi + mi
    if k % 7 == 3: print(i, k)
