def fibonacciSequence(n):
    a = 0
    b = 1
    c = 0
    while c <= n:
        print(a)
        a, b = b, a + b
        c += 1
        
fibonacciSequence(10)
