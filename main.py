# module_2_4.ru

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []

for i in numbers:
    if i<2: continue
    is_prime = True
    for j in range(2, i-1):
        if i % j == 0:
            is_prime = False
            break               #добавление этого оператора значительно ускоряет поиск
    if is_prime == False:
        no_primes.append(i)
    else:
        primes.append(i)

print('Primes', primes)
print('No primes', no_primes)

# module_2_4.ru

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []

for i in numbers:
if i<2: continue
is_prime = True
for j in range(2, i-1):
if i % j == 0:
is_prime = False
break #добавление этого оператора значительно ускоряет поиск
if is_prime == False:
no_primes.append(i)
else:
primes.append(i)

print('Primes', primes)
print('No primes', no_primes) 