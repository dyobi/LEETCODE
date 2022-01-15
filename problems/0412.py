"412. Fizz Buzz"

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Input: n = 15 / Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = []

        for i in range(1, n + 1):
            if (i % 15 == 0):
                res.append("FizzBuzz")
            elif (i % 3 == 0):
                res.append("Fizz")
            elif (i % 5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))

        return res
