# LZ77 decoding 
# It's straightforward since you have the commands in each tuple to tell you how to reconstruct the text

def lz77_decode(encoded):
    decoded = ""
    for distance, length, char in encoded:
        if distance == 0:
            decoded += char
        else:
            start = len(decoded) - distance
            for i in range(length):
                decoded += decoded[start + i]
            decoded += char
    return decoded

decoded = lz77_decode(encoded)
print("Decoded:", decoded)
