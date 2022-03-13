import math
################ ROZDIZAł 1 ################
# konwersacja liczby dziesiętnej w binarną
# def dec_to_bin (num):
#     if num > 0:
#         dec_to_bin(num//2)
#         print(num%2,end="")

# num = int(input())
# dec_to_bin(num)
# print()

# konwersacja dowolnego systemu liczbowego
# OLD
# def calc_any_num_sys(num, sys):
#     if sys > 26:
#         return 0
#     num_list = {}
#     first_chr = ord("A")
#
#     for i in range(sys):
#         if i >= 10 and i <= 26:
#             num_list[i] = chr(first_chr)
#             first_chr += 1
#         else:
#             num_list[i] = i
#
#     if num > 0:
#         calc_any_num_sys(num // sys, sys)
#         r = num_list[num % sys]
#         print(r, end="")


# konwersacja dowolnego systemu liczbowego
# 1)
# dec_numbers = [15, 12, 2, 4, 7, 8]
# dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
# dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
# dec_TO_hex = [hex(i)[2:] for i in dec_numbers]
#
# bin_TO_dec = [int(i, 2) for i in dec_TO_bin]
# oct_TO_dec = [int(i, 8) for i in dec_TO_oct]
# hex_TO_dec = [int(i, 16) for i in dec_TO_hex]
#
# print(dec_TO_bin, dec_TO_oct, dec_TO_hex)


# 2)
# def calc_any_num_sys(num, sys):
#     BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if num < sys:
#         return BS[num]
#     return calc_any_num_sys(num // sys, sys) + BS[num % sys]
#
# num = int(input())
# s = int(input())
# print(calc_any_num_sys(num, s))


################ ROZDIZAł 2 ################
#import math
#czy liczba jest pierwsza
# def is_prime(X):
#     num_sqrt = round(math.sqrt(x)) + 1
#     if x > 1:
#         for i in range(2, num_sqrt):
#             if x % i == 0:
#                 return False
#         return True
#     return False


################ ROZDIZAł 3 ################
# 11.02.22
# czy liczba jest liczbą doskonałą
"""
Liczba dosonala - liczba, której suma jej dzielników (bez niej samej) jest jej równa
"""
"""def czy_doskonala(n):
    s = 1
    p = int(math.sqrt(n))

    for i in range(2, p+1):
        print(i)
        if (n%i == 0):
            s+=i+n/i
    print(s)
    if (n == p**2):
        s -= p

    if (n==s):
        return 1

    return 0

print(czy_doskonala(6))"""


################ ROZDIZAł 4 ################
# 12.03.22
# Rozkładanie liczb na czynniki pierwsze

# mój algorytm
"""def prime_factors(n):
    k = 2
    while n!=1:
        if (n%k==0):
            n=n//k
            print(k)
        else:
            k+=1"""

"""def prime_factors(n):
    k = 2
    pierw = int(math.sqrt(n))
    liczba_pierw = 1
    while n != 1 and k <= pierw:
        while n % k == 0:
            liczba_pierw = 0
            n = n//k
            print(k)
        k += 1
    if (liczba_pierw):
        print(n)
    if (k >= pierw):
        print(1)

prime_factors(17)"""








