import random


def private_key(p):
    g = random.randint(2, 50000)
    return (g ** p) % p


def public_key(pk, p, g):
    return (g ** pk) % p


def secret_key(pk, pb, p):
    return (pb ** pk) % p
