# function sumOfNPrimes(n) {
#   let sum = 0;
#   let primes = firstNPrimes(n);

#   for (let i = 0;  i < primes.length; i += 1) {
#       sum += primes[i];
#   }

#   return sum;
# }

def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)

    for i in range(len(primes.length)):
        sum += primes[i]

    return sum