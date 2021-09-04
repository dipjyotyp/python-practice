def encrypt(text, n):
    if n <= 0:
        return text
    if not text:
        return text
    for steps in range(n):
        even_arr = []
        odd_arr = []
        for i in range(0, len(text)):
            if i % 2 == 0:
                even_arr.append(text[i])
            else:
                odd_arr.append(text[i])
        new_text = odd_arr + even_arr
        text = ''.join(new_text)
 
    return text

def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    if not encrypted_text:
        return encrypted_text
    for steps in range(n):
        odd_text = encrypted_text[:int(len(encrypted_text)/2)]
        even_text = encrypted_text[int(len(encrypted_text)/2):]
        final_message = []
        for i in range(len(encrypted_text)):
            try:
                final_message.append(even_text[i])
                final_message.append(odd_text[i])
            except IndexError:
                pass
        encrypted_text = ''.join(final_message)
    return encrypted_text
        



print(encrypt('This kata is very interesting!', 5))
print(encrypt("This is a test!", 4))
print(encrypt("This is a test!!", 8))
print(encrypt("WOT", 1))

print(decrypt("hsi  etTi sats!", 1))
print(decrypt(" Tah itse sits!", 3))
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))