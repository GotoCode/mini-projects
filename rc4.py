#
# rc4.py - A python implementation of the RC4 stream cipher
#


# external modules #

from sort import swap
import copy


# helper functions #


# key-scheduling algorithm (KSA) #

def init_byte_array(byte_array, key):

    my_byte_array = copy.deepcopy(byte_array)

    key_length = len(key)

    j = 0

    for i in range(0, 256):

        j = (j + my_byte_array[i] + ord(key[i % key_length])) % 256

        swap(my_byte_array, i, j)

    return my_byte_array


# Pseudo-Random Generation Algorithm (PRGA) #

def get_keystream(len_stream, byte_array):

    key_stream = ""

    i = j = 0

    for k in range(0, len_stream):

        i = (i + 1)             % 256
        j = (j + byte_array[i]) % 256

        key_byte = byte_array[(byte_array[i] + byte_array[j]) % 256]

        key_stream += chr(key_byte)

    return key_stream



# main functions #


# encode plaintext using RC4 #

def encode(plaintext, key_text):

    key = key_text[:256]

    byte_array = init_byte_array(range(0, 256), key)

    key_stream = get_keystream(len(plaintext), byte_array)

    ciphertext = ""

    for i in range(len(plaintext)):

        ciphertext += chr(ord(plaintext[i]) ^ ord(key_stream[i]))

    return ciphertext


# decode ciphertext using RC4 #

def decode(ciphertext, key_text):

    return encode(ciphertext, key_text)
