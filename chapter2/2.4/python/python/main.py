import sys

def gcd(n: int, m: int) -> int:
    assert (n != 0) & (m != 0), "n and m must be non-zero"
    while m != 0: 
        if m < n :
            t = m
            m = n
            n = t
        m = m % n
    return n

def main():
    numbers = sys.argv
    if len(numbers) == 1:
        raise Exception("No arguments")
    d = numbers[1]
    for m in numbers[2:]:
        d = gcd(int(d), int(m))
    print(f"The greatest common divisor of {numbers[1:]} is {d}")

if __name__ == '__main__':
    main()