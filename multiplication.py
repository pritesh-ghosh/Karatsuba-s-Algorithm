# MULTIPLICATION OF TWO NUMBERS USING KARATSUBA'S ALGORITHM
# NUMBERS ARE (A) 3141592653589793238462643383279502884197169399375105820974944592 
# AND (B) 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x, y):
    # Convert numbers to strings for easy manipulation
    x = str(x)
    y = str(y)
    
    # Base case: if the numbers are small, multiply directly
    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)
    
    # Pad the shorter number with leading zeros
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    
    # Split the numbers into halves
    n = len(x)
    half = n // 2
    
    a = x[:half]
    b = x[half:]
    c = y[:half]
    d = y[half:]
    
    # Recursively compute ac, bd, and (a+b)(c+d)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(str(int(a) + int(b)), str(int(c) + int(d))) - ac - bd
    
    # Combine the results
    result = ac * 10 ** (2 * (n - half)) + ad_plus_bc * 10 ** (n - half) + bd
    return result

# Input numbers
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

# Compute the product
product = karatsuba(x, y)
print(product)
