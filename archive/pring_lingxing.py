for i in range(1,21):
	for j in range(1,21-i):
		print(' ', end='')
	for j in range(1, i):
		print('/', end='')
	for j in range(1, i):
		print('*', end='')
	print()
for i in range(1,21):
	for j in range(1, i):
		print(' ', end='')
	for j in range(1, 21-i):
		print('+', end='')
	for j in range(1, 21-i):
		print('-', end='')
	print()