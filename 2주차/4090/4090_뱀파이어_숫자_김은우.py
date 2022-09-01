#미완료
from itertools import permutations
import sys
input = sys.stdin.readline
def search(x):
    while True:
        y = str(x)
        l = len(y)

        for perm in permutations(y, l):
            if perm[0] == '0' :
                continue
            
            num = int(''.join(perm))            
            for i in range(1, l):
                print(num%(10**i), num//(10**i), num%(10**i) * num//(10**i), x)
                if (num%10**i) * (num//10**i) == x :
                    return x
        x += 1

while (x := int(input())) != 0:
    print(search(x))