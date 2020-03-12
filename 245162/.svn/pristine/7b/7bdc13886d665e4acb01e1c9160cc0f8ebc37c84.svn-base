import math
import random
from math import log


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def findPrimes(bits):
    length = int(log(2) / log(10) * bits)
    p = random.getrandbits(length)
    q = random.getrandbits(length)
    while not is_prime(p):
        p = random.getrandbits(length)
    while not is_prime(q) or q == p:
        q = random.getrandbits(length)
    return p, q


def generate_keypair(bits):
    p, q = findPrimes(bits)
    print(p, q)
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # 1
    n = p * q

    # 2
    phi = (p - 1) * (q - 1)

    # 3
    e = random.randrange(1, phi)

    # 4
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    # 5
    d = multiplicative_inverse(e, phi)

    # Public (e, n), private(d, n)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


def is_prime(n):
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


public, private = generate_keypair(128)
print(public, private)
message = input("Enter a message to encrypt with your private key: ")
encrypted_msg = encrypt(private, message)
print("Your encrypted message is: ", encrypted_msg)
print(''.join(map(lambda x: str(x), encrypted_msg)))
print("Decrypting message with public key ", public, " . . .")
decrypted_msg = decrypt(public, encrypted_msg)
print("Your message is:", decrypted_msg)
