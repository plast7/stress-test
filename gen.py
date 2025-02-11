from randomfactory import *
n = generate_integer(2, 5)
m = generate_integer(2, 5)
q = generate_integer(1, 5)

arr = generate_2d_array(n, m, 0, 5)

print(n, m, q)

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()

cnt = 0
while cnt < q:
    row = generate_integer(1, n)
    dir = 'L' if generate_integer(0, 1) == 0 else 'R'
    print(row, dir)
    cnt += 1