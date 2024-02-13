class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

# Основна функція для реалізації кодування Хаффмана
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    dictionary = dict()
    dictionary.update(huffman_code_tree(l, True, binString + '0'))
    dictionary.update(huffman_code_tree(r, False, binString + '1'))
    return dictionary

# Функція для розкодування Хаффмана
def huffman_decode(encoded_string, huffman_code):
    decoded_string = ""
    current_code = ""
    for bit in encoded_string:
        current_code += bit
        for char, code in huffman_code.items():
            if code == current_code:
                decoded_string += char
                current_code = ""
                break
    return decoded_string

# Заданий рядок для розкодування
string = 'Huffman'

# Обчислення частот
frequencies = {}
for char in string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

nodes = frequencies

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = TreeNode(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

# Закодування та розкодування
encoded_string = ''.join(huffmanCode[char] for char in string)
decoded_string = huffman_decode(encoded_string, huffmanCode)

print('Оригінальний рядок:', string)
print('Закодований рядок:', encoded_string)
print('Розкодований рядок:', decoded_string)
