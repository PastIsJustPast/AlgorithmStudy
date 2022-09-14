import math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    word = ""
    while n:
        word = str(n % k) + word
        n = n // k
    word = word.split("0")
    cnt = 0

    for w in word:
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        if is_prime(int(w)):
            cnt += 1

    return cnt