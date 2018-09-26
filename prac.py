res = 0


def fac(num):
    if num == 1:
        return 1
    else:
        res = num * fac(num - 1)
        return res
