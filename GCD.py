def gcd(x,y):
    # Swap to the largest number for the division
    if x < y:
        x, y = y, x
    # If Y = 0 then GCD(X,Y) = X
    if y == 0:
        return x
    return gcd(y, x%y)

if __name__ == '__main__':
    print(gcd(1680, 640))
