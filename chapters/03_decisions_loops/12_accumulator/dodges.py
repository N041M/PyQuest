# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("sum() over a comprehension instead of an accumulator loop",
     "n = int(input())\n"
     "nums = [int(input()) for _ in range(n)]\n"
     "print(sum(nums))\n"),
]
