import time

def factorial(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n-=1
    return respuesta

def facorial_r(n):
    if n==1:
        return1
    return n*factorial(n-1)

if __name__ == '__main__':
    n= 200000
    comienzo = time.time()
    print(factorial(n))
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    facorial_r(n)
    final = time.time()
    print(final - comienzo)