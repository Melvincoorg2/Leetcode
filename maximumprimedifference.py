class Solution:
 def maximumPrimeDifference(self, nums: List[int]) -> int:

    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True

    primes = [i for i, x in enumerate(nums) if is_prime(x)]
    return primes[-1] - primes[0]