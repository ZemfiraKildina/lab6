k = 0
for x in range(452022, 1000000):
    a = []
    for D in range(2,x):
        if x % D == 0:
            a.append(D)
            if len(a) >= 2:
                M = a[0] + a[-1]
            else:
                M = 0
    if M % 7 == 3:
        k += 1
        print(x , M)
    if k == 5:
        break