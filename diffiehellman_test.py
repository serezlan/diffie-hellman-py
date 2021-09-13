from diffiehellman import private_key, public_key, secret_key


class DFTest:
    def __init__(self, g, p, pk1, pk2, pb1, pb2, s):
        # Generator
        self.g = g
        # common key, modulus
        self.p = p
        # private keys
        self.pk1 = pk1
        self.pk2 = pk2
        # public keys
        self.pb1 = pb1
        self.pb2 = pb2
        # Secret key
        self.s = s


testcase = DFTest(5, 23, 6, 15, 8, 19, 2)


def test_private_key():
    actual = private_key((testcase.p))

    assert actual > 1 and actual < testcase.p


def test_always_generate_random_private_key():
    keys = {}

    for i in range(10):
        keys[private_key(testcase.p)] = True

    assert len(keys) != 1


def test_public_key():
    expected = testcase.pb1

    actual = public_key(testcase.pk1, testcase.p, testcase.g)

    assert expected == actual


def test_secret_key():
    expected = testcase.s

    actual = secret_key(testcase.pk1, testcase.pb2, testcase.p)

    assert expected == actual
