# python3 30840 KB, 18552 ms
# pypy3 117312 KB, 4212 ms

def get_digits(number):
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    return sorted(digits)


def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= n:
            end = mid -1
        else:
            start = mid + 1
    return start


vampires = set()
for i in range(2, 10 ** 6):
    i_digits = get_digits(i)
    for j in range(i, 10 ** 6):
        left = i * j
        if left > 1.1 * (10 ** 6):
            break
        j_digits = get_digits(j)
        right_digits = sorted(i_digits + j_digits)
        left_digits = get_digits(left)
        if left_digits == right_digits:
            vampires.add(left)
vampires = list(vampires)
vampires.sort()

while True:
    n = int(input())
    if n == 0:
        break
    idx = binary_search(vampires, n)
    print(vampires[idx])
