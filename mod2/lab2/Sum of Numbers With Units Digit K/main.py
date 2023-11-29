def min_set_size(num, k):
    if num == 0:
        return 0
    if k == 0:
        if num%10 == 0:
            return 1
        return -1
    count = 1
    while num%10 != k and num > 0:
        num -= k
        count += 1
    if num > 0 and num %10 == k:
        return count
    return -1


num = 58
k = 9
result = min_set_size(num, k)
print(result)