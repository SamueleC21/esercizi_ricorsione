
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n-1)

def factorial_samu(n):
    if n == 0 or n == 1:
        return 1
    else:
        r = factorial_samu(n-1)
        fattoriale = n * r
        return fattoriale


if __name__== '__main__':
    N = 7
    print(factorial(N))

    print("prova", factorial_samu(N))