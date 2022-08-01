
from secrets import token_bytes

def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original):
    original_bytes = original.encode() # 들어온 글자를 bytes 로 변경함.
    dummy = random_key(len(original_bytes)) # 해당 bytes의 길이를 넣으면 b'\xf9\xca\x8a9\x01\x90\x1f<\xf47\x7f6' 이런 꼴로 변경됨
    original_key = int.from_bytes(original_bytes, "big") # 34486295488025848092598231396
    print(original_key, type(original_key), dummy, type(dummy))
    encrypted = original_key ^ dummy #
    return dummy, encrypted

def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7)//8, "big")
    return temp.decode()

if __name__=="__main__":
    key1, key2 = encrypt("One Time pad")
    print(key1, key2)
    result = decrypt(key1, key2)
    print(result)



