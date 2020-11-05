#!/bin/python3

n = int(input())

# Jika n ganjil, cetak Weird
if n % 2 == 1:
    print("Weird")
    
# Jika n genap dan dalam kisaran inklusif 2 hingga 5, cetak Not Weird
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
    
# Jika n genap dan dalam kisaran inklusif 10 hingga 18, cetak Weird
elif n % 2 == 0 and 10 <= n <= 18:
    print("Weird") 
    
# Jika n genap dan dalam kisaran inklusif 6 hingga 20, cetak Weird
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
    
# Jika n lebih besar dari 20, cetak Not Weird
else:
    print("Not Weird")

