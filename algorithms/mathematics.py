
# O(log n)
def pow(a, n):
    x = 1
    while n:
        if n % 2:
            x *= a
        a, n = a * a, n // 2
    return x


# O(log(a + b))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

