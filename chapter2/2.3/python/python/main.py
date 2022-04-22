def gcd(n: int, m: int) -> int:
    assert (n != 0) & (m != 0), "n and m must be non-zero"
    while m != 0: 
        if m < n :
            t = m
            m = n
            n = t
        m = m % n
    return n

if __name__ == '__main__':
    print(gcd(14, 15))
