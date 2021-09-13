import random


def new_pair(p, g):
    pk = private_key(p)
    pb = public_key(pk, p, g)
    return pk, pb


def private_key(p):
    k = 0
    while k <= 1:
        g = random.randint(2, 50000)
        k = (g ** p) % p
    return k


def public_key(pk, p, g):
    return (g ** pk) % p


def secret_key(pk, pb_r, p):
    return (pb_r ** pk) % p


def my_test():
    g = 2
    p = 19
    pk1, pb1 = new_pair(p, g)
    pk2, pb2 = new_pair(p, g)
    print("keypair 1:", pk1, pb1)
    print("keypair 2:", pk2, pb2)
    s1 = secret_key(pk1, pb2, p)
    s2 = secret_key(pk2, pb1, p)
    print("s", s1, s2)
