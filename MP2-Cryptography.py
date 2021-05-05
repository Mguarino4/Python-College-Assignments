def shift(ch,k):
    return chr(ord('a')+(ord(ch)-ord('a')+k)%26)

print(shift('w',5))


def char_encrypt(plaintextchar, keychar):
    k = ord(keychar) - 97
    ch = plaintextchar
    return chr(ord('a')+(ord(ch)-ord('a')+k)%26)

print(char_encrypt('w','f'))


def char_decrypt(cipherchar, keychar):
    k = ord(keychar) - 97
    ch = cipherchar
    return chr(ord('a')+(ord(ch)-ord('a')-k)%26)

print(char_decrypt('b','f'))


def pre_process(s):
    x = s.replace(" ", "")
    z = x.lower()
    return z

print(pre_process("Happy B-Day"))


def vig_encrypt(plaintext, key):
    plaintext="We'rehavingaparty"
    plain = pre_process(plaintext)
    new = ""
    for i in plain:
        new += char_encrypt(i, key)
    return new


def vig_encrypt(new):
    new=vig_encrypt('')
    for new in vig_encrypt('', key)
        new +=char_decrypt()