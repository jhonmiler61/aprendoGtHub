#Ley de la Multiplicación

def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

f(20)

#O(n)* O(n) = O(n*n) = O(n**2)