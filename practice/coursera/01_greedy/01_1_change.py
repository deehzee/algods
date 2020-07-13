# Uses python3


def get_change(m):
    coins = [10, 5, 1]
    n = 0
    i = 0
    while m > 0:
        while coins[i] > m:
            i += 1
        n += m // coins[i]
        m %= coins[i]
    return n


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

