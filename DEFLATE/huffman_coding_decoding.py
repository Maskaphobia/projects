# Huffman decoding
# The only reason why Huffman decoding works is because it's a form of prefix code
# No code is a PREFIX of another code
# Try decoding the Huffman code if 's' : '1'. It's not possible :]

# For those that are sharp, different files using huffman encoding creates a different tree (since frequency is different)
# So how is it possible that my file explorer can decode/unzip a random zipped file?
# In fact, the image contains metadata on the frequency count (calculate_frequency()), allowing it to recreate the tree and reverse it
def huffman_decoding(encoded, codes):
    decoded = []
    current_code = ''
    code_to_char = {v: k for k, v in codes.items()} # Invert the codes
    for bit in encoded:
        current_code += bit
        if current_code in code_to_char: # Matched bits to known combination in dictionary
            decoded.append(code_to_char[current_code])
            current_code = '' # Reset
    return ''.join(decoded)
decoded = huffman_decoding(encoded, codes) # As you can see, we need two parameters.
print("Decoded text: ", decoded) # Although you have the encoded message, you need to know the conversion table/codes or we can't decode it
