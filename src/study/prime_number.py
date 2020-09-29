# 素数表示（https://spjai.com/python-tutorial/#7-4）
prime_list = []
for i in range(2,1000):
    is_prime = True
    for prime in prime_list: 
        if i % prime==0: 
            is_prime=False
    if is_prime:
        print(i)
        prime_list.append(i)