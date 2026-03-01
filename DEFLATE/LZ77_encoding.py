# LZ77 encoding
# Intuition: Suppose we have seen a particular substring, but repeating it wastes bit size
# Solution: We can just mention where to find it in the original string
# Pre requesite: Sliding window 

def lz77_encode(data, window_size=50):
    i = 0
    output = []

    while i < len(data):
        max_length = 0
        max_distance = 0
        start = max(0, i - window_size)
        for j in range(start, i):

            length = 0
            while i + length < len(data) and data[j + length] == data[i + length]:
                length += 1

            if length > max_length:
                max_length = length
                max_distance = i - j

        # If match found
        if max_length > 0:
            next_char = data[i + max_length] if i + max_length < len(data) else ''
            output.append((max_distance, max_length, next_char)) 
            i += max_length + 1
        else:
            output.append((0, 0, data[i]))
            i += 1

    return output

text = "never gonna give you up never gonna let you down"
encoded = lz77_encode(text)
print('Original: ', text)
print('Encoded: ', encoded)
print('This makes decoding also much easier.')
# In fact, there aren't many python implementation on this because it's quite inefficient and it is mainly in C
# Thus, this code main purpose is to understand the logic rather than the code implementation: 
# Each LZ77 tuple is (distance, length, next_char), where distance = current - match_position, length is how many characters to copy, next_char is the next char
# So we go back, copy the longest match then append the next new character
# (24, 11, 'l') effectively reconstructs "never gonna l" since 'never gonna ' is a repeated substring
# Isolating it, it basically does "never gonna give you up (Go back 24 tuples, Copy 11, Append 'l')et you down"
