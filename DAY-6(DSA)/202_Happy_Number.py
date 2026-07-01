class Solution:
    def isHappy(self, n: int) -> bool:

        v = set()

        while n != 1 and n not in v:

            v.add(n)

            t = 0

            while n > 0:

                d = n % 10

                t += d * d

                n //= 10

            n = t

        return n == 1