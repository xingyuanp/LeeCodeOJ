class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        sieve = n * [1]
        sieve[0] = sieve[1] = 0
        for factor in range(2, int(n**0.5) + 1):
            if sieve[factor] == 1:
                length = len(sieve[factor**2:n:factor])
                sieve[factor**2:n:factor] = length * [0]
        return sum(sieve)