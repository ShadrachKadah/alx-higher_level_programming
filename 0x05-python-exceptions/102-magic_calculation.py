#!/usr/bin/python3
def magic_calculation(x, y):
    result = 0
    for f in range(1, 3):
        try:
            if f > x:
                raise Exception('Too far')
            result += x ** y / f
        except Exception:
            result = y + x
            break
    return result
