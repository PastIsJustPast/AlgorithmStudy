def ten2k(n,q):
    rev_base = ''
    while n > 0:
        rev_base += str(n%q)
        n //= q
    return rev_base[::-1]



def check_prime(number):
    if number <=1 : return False
    i = 2
    while i*i <= number:
        if number %  i == 0 : #나누어떨어지면
            return False
        i+=1
    return True

def solution(n,k) :
    answer = 0
    num = ten2k(n,k)
    for info in num.split("0"): #으로 구분하기
        if not info : continue
        if check_prime(int(info)):
            answer +=1
    return answer