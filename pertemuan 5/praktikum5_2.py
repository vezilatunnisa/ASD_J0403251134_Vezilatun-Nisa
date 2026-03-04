def hitung(n):
    if n == 0:
        print("Selesai")
        return 
    print("masuk", n)
    hitung(n - 1)
    hitung(n-1)
    print("keluar", n)
    
print("======program tracing======")
hitung(5)