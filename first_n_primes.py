# function firstNPrimes(n) {
#     const primes = [];
#     let num = 2;
  
#     while(primes.length < n) {
#       if (isPrime(num)) {
#         primes.push(num);
#       }
  
#       num += 1;
#     }
  
#     return primes;
# }

def first_n_primes(n):
    primes = []
    num = 2
    while primes.length < n:
        if is_prime(num):
            primes.append(num)
        num +=1
    return primes