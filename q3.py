num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def sieve_of_eratosthenes(num_list):
    is_prime = [True] * (max(num_list) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max(num_list)**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max(num_list)+1, i):
                is_prime[j] = False
    prime_list = []
    for num in num_list:
        if is_prime[num]:
            prime_list.append(num)
    return prime_list

prime_list = sieve_of_eratosthenes(num_list)
print(prime_list)
