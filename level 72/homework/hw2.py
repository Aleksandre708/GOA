def is_triangle(a, b, c):
    # Check all sides are greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Check triangle inequality
    return a + b > c and a + c > b and b + c > a
