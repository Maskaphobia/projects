# Huffman encoding
# Intuition: Suppose you have a string, and some characters appear more frequently than others, but all of them takes up the same bit size (E.g. 'looool' -> 110110011011111101111110111111011111101100)
# Solution: We can prioritise them based on frequency, with the smallest bit size being the most common and the largest bit size being the rarest (E.g. 'looool' -> 011110)
# Prerequisite: Binary trees, Priority Queue/Min Heap* [Not necessary to implement]

import heapq # min-heap

class Node:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None
    def __lt__(self, other): # Needed for heapq to compare nodes
        return self.freq < other.freq

def calculate_frequency(word): # Creating a dictionary to store frequency, important for decoding
    frequency = {}
    for i in word:
        if i not in frequency:
            frequency[i] = 0
        frequency[i] += 1
    return frequency
def create_nodes(frequency): # Creating individual nodes
    nodes = []
    for key in frequency:
        nodes.append(Node(frequency[key], key))
    return nodes # E.g. Node('l': 2), Node('o': 1), Node('s': 4), Node('e': 1)

def build_huffman_tree(nodes): # Linking the nodes together, parent node is the sum of the frequency children nodes, without a character
    while len(nodes) > 1: # Merge two smallest nodes until one remains
        left = heapq.heappop(nodes) # The point is to get the rarest/smallest frequency of the character to be at the bottom. That's why min-heap is good
        right = heapq.heappop(nodes) # Of course, you can sort repeatedly but that's inefficient  ¯\_(ツ)_/¯

        merged = Node(left.freq + right.freq, None)
        merged.left = left
        merged.right = right

        heapq.heappush(nodes, merged)

    return nodes[0] # Your root/top of the tree. Subsequently becomes parent of children nodes

def generate_codes(node, current_code, codes): # Assigning binary through recursive traversal
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    # Traversal left
    generate_codes(node.left, current_code + '0', codes)

    # Traversal right
    generate_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    codes = {}
    frequency = calculate_frequency(word)
    nodes = create_nodes(frequency)
    root = build_huffman_tree(nodes)
    generate_codes(root, "", codes) # (Current node in huffman tree, the code accumulated so far, codes/dictionary)
    return codes

word = "lossless"
binary = ''
dictionary = {}
for i in word:
    char = bin(ord(i))[2:]
    binary += char
    if i not in dictionary:
        dictionary[i] = char
encoded = ''
codes = huffman_encoding(word)
encoded = ''.join(codes[c] for c in word)

print("UTF-8: ", binary)
print("UTF-8 conversion table: ", dictionary)
print("Huffman code: ", encoded)
print("Huffman conversion table: ", codes)
print("As you can see, it stores the same text with fewer bits.")

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
