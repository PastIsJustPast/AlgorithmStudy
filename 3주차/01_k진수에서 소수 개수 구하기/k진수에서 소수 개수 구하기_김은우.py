import math
def is_prime(n):
    if not n :
        return False
    else :
        n = int(n)
        
    if n < 2 :
        return False 
        
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True

def solution(n, k):
    nota = ''
    #n진법으로 변환
    while n != 0 :
        nota = str(n%k) + nota
        n //= k

    return sum(is_prime(i) for i in nota.split('0'))