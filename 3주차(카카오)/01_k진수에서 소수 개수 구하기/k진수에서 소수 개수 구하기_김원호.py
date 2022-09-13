def to_k_nary(n, k):
    k_nary = ''
    while n:
        n, r = divmod(n, k)
        k_nary = str(r) + k_nary
    return k_nary


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def solution(n, k):
    k_nary = to_k_nary(n, k)
    candidates = k_nary.split('0')
    candidates = [candidate for candidate in candidates if candidate]
    candidates = [candidate for candidate in candidates if is_prime(int(candidate))]
    answer = len(candidates)
    return answer