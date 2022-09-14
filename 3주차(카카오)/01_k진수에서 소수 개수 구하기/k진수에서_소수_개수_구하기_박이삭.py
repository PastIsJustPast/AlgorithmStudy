def solution(n, k):
    answer = 0
    k_n = k_nary(n, k)
    print(k_n)
    for num in map(lambda x : int(x) if x else 0, k_n.strip("0").split("0")):
        answer += isprime(num)
    return answer

def k_nary(n, k):
    k_n = ""
    q, r = divmod(n, k)
    k_n = str(r) + k_n
    while q:
        q, r = divmod(q, k)
        k_n = str(r) + k_n
    return k_n
        
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int((n + 1)**.5) + 1):
        if n % i == 0:
            return False
    return True