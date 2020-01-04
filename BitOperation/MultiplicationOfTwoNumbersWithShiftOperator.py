# https://www.geeksforgeeks.org/multiplication-two-numbers-shift-operator/

'''
25 * 13 = 25 * 8 + 25 * 4 + 25 * 1
        = 25 << 3 + 25 << 2 + 25 << 0
'''

def multiply(n, m):
    res, bitcount = 0, 0
    while m:
        if m % 2 == 1:
            res += (n << bitcount)

        bitcount += 1
        m = m >> 1

    return res
    
