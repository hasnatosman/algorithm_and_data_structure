"""n = int(input('Input a number: '))

if n % 2 == 0:
    print('Even')
else:
    print('Odd')
"""
n = 5
even = [False] * (n+1)
for i in range(2, n+1, 2):
    even[i] = True

print(even)