f = open('17.txt')
a = [int(i) for i in f]
s = 0
mx = 0
sum = 0
count = 0
for i in range(len(a)):
    if (a[i] % 2 == 1):
        sum += a[i]
        count += 1
x = sum / count
for i in range(len(a) - 1):
    if ((a[i] % 5 == 0) or (a[i + 1] % 5 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        s += 1
        mx = max(mx, a[i] + a[i + 1])
print(s, mx)
