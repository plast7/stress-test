from random import randint

n = randint(1, 100)
k = randint(1, 100)

arr = [
	randint(1, 100) for _ in range(n)
]

print(n, k)
for elem in arr:
	print(elem, end=" ")