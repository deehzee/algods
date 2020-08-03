# Uses python3
import sys

### Solution 0: Brute Force ###


def get_change_bruteforce(m, coins):
    if m <=0:
        return 0
    n = m // min(coins) + 1
    for c in coins:
        if m >= c:
            n = min(n, 1 + get_change_bruteforce(m - c, coins))
    return n


### Solution 1: Memoization ###


def memoize(func):
    tab = {}
    def memoized_func(m, coins):
        if m not in tab:
            tab[m] = func(m, coins)
        return tab[m]
    return memoized_func


@memoize
def get_change_memoize(m, coins):
    if m <=0:
        return 0
    n = m // min(coins) + 1
    for c in coins:
        if m >= c:
            n = min(n, 1 + get_change_bruteforce(m - c, coins))
    return n


### Solution 2: Dynamic Programming ###


def get_change_dynprog(m, coins):
    # tab[i] = min num of coins needed to make i
    tab = [None] * (m + 1)
    min_denom = min(coins) # min denomination
    # Initial values
    tab[0] = 0
    # Compute bottom up
    for i in range(1, m + 1):
        tab[i] = i // min_denom + 1
        for c in coins:
            if i >= c:
                tab[i] = min(tab[i], 1 + tab[i - c])
    return tab[-1]


### Main ###

get_change = get_change_dynprog


def main():
    m = int(input())
    coins = [1, 3, 4]
    print(get_change(m, coins))


if __name__ == '__main__':
    main()

