# A simple form of Huffman coding using lists and tuples
line = "I Miss Mississippi."

def convert_to_freq_list(line):
  # For example, the line is "I Miss Mississippi."
  # this function returns a list of the following
  # [[1, 'I'], [1, '.'], [2, ' '], [2, 'M'], [2, 'p'], [5, 'i'], [6, 's']]
  # Each element in this list can be considered a node of the Huffman tree 
    mydict = {}
    lst= []
    for letter in line: 
        if letter not in mydict: 
            mydict[letter] = 1
        else:
            mydict[letter] += 1
    asc = {k: v for k, v in sorted(mydict.items(), key=lambda item: item[1])}
    for values, keys in asc.items():
        lst.append([keys, values])
    return lst
freq_list = convert_to_freq_list(line)
print(freq_list)


def create_hf_bt(freq_list):
    nodes = [(freq, char) for freq, char in freq_list] # Turning each node into a tuple 
    while len(nodes) > 1: # Stops when all nodes are combined together (and total frequency is summed up) 
        nodes = sorted(nodes, key = lambda x:x[0]) # Sort the list so that the first two nodes has the smallest frequency
        f1, left = nodes.pop(0) 
        f2, right = nodes.pop(0)
        new_node = (f1+f2, [left, right]) # Sum of frequency, (left node, right node) 
        nodes.append(new_node) 
    return nodes[0][1] # Removes the total frequency count 
hf_bt = create_hf_bt(freq_list)
print(hf_bt)
# output = [[[' ', 'M'], ['p', ['I', '.']]], ['i', 's']]

# Recursion version (Similar logic)
def create_hf_bt_rec(freq_lst):
    if len(freq_lst) == 1:
        return freq_lst[0][1]
    else:
        freq_lst = sorted(freq_lst, key = lambda x:x[0])
        f1, left = freq_lst.pop(0)
        f2, right = freq_lst.pop(0)
        new_node = (f1+f2, [left, right])
        new_lst = freq_lst + [new_node]
        return create_hf_bt_rec(new_lst)

hf_bt = create_hf_bt_rec(freq_list)
print(hf_bt)
