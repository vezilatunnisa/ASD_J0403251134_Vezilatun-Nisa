def faktorial(n):
    if n == 0:
        return 1
    
    return n * faktorial(n - 1)
print("======program faktorial======")
print("hasilfaktorial: ",faktorial(2))
