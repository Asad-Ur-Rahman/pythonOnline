def fact_rec(n):

    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)