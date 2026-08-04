def fib2(n):
    '''nより小さなフィボナッチを数列を列挙で返す'''
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

print(fib2(1000))
