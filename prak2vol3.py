"no 3"
def fibonacci(n):
    a, b = 0,1
    hasil = []
    while a <= n :
        hasil.append(a)
        a, b = b, a + b
    return hasil
n = int(input("masukan bilangan:"))
print("hasil:", fibonacci(n))