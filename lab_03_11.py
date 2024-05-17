import os
import heapq
from collections import defaultdict, Counter, namedtuple


class HuffmanNode(namedtuple("HuffmanNode", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class HuffmanLeaf(namedtuple("HuffmanLeaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def build_tree(freq):
    heap = []
    for char, frequency in freq.items():
        heap.append((frequency, len(heap), HuffmanLeaf(char)))
    heapq.heapify(heap)

    count = len(heap)
    while len(heap) > 1:
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, count, HuffmanNode(left, right)))
        count += 1

    return heap[0][-1]


def huffman_code(tree):
    code = {}
    tree.walk(code, "")
    return code


def encodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            text = f.read()

        freq = Counter(text)
        tree = build_tree(freq)
        code = huffman_code(tree)

        encoded_text = ''.join(code[char] for char in text)
        padding = 8 - len(encoded_text) % 8
        encoded_text += '0' * padding
        padded_info = "{0:08b}".format(padding)

        b = bytearray()
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i + 8]
            b.append(int(byte, 2))

        with open(fileOut, 'wb') as f:
            f.write(bytes(padded_info, 'utf-8'))
            f.write(b)

        with open(fileOut + ".freq", 'w') as f:
            for char, frequency in freq.items():
                f.write(f"{char}:{frequency}\n")

        return True
    except Exception as e:
        print(f"An error occurred during Huffman encoding: {e}")
        return False


def decodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'rb') as f:
            padded_info = f.read(1)
            padding = int(padded_info, 2)
            encoded_text = ""
            byte = f.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                encoded_text += bits
                byte = f.read(1)

        encoded_text = encoded_text[:-padding]

        freq = {}
        with open(fileIn + ".freq", 'r') as f:
            for line in f:
                parts = line.rstrip().split(':')
                if len(parts) == 2:
                    char, frequency = parts
                    freq[char] = int(frequency)

        tree = build_tree(freq)
        code = huffman_code(tree)

        inv_code = {v: k for k, v in code.items()}
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in inv_code:
                character = inv_code[current_code]
                decoded_text += character
                current_code = ""

        with open(fileOut, 'w') as f:
            f.write(decoded_text)

        return True
    except Exception as e:
        print(f"An error occurred during Huffman decoding: {e}")
        return False


def encodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            text = f.read()

        dictionary = {}
        data = []
        phrase = ""
        dict_size = 1

        for char in text:
            phrase_char = phrase + char
            if phrase_char in dictionary:
                phrase = phrase_char
            else:
                if phrase:
                    data.append((dictionary[phrase], char))
                else:
                    data.append((0, char))
                dictionary[phrase_char] = dict_size
                dict_size += 1
                phrase = ""

        with open(fileOut, 'w') as f:
            for pair in data:
                f.write(f"{pair[0]} {pair[1]}\n")

        return True
    except Exception as e:
        print(f"An error occurred during LZ encoding: {e}")
        return False


def decodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'r') as f:
            data = f.readlines()

        dictionary = {}
        dict_size = 1
        decoded_text = ""

        for line in data:
            parts = line.split()
            if len(parts) == 2:
                index, char = parts
                index = int(index)

                if index == 0:
                    phrase = ""
                else:
                    phrase = dictionary[index]

                decoded_text += phrase + char
                dictionary[dict_size] = phrase + char
                dict_size += 1

        with open(fileOut, 'w') as f:
            f.write(decoded_text)

        return True
    except Exception as e:
        print(f"An error occurred during LZ decoding: {e}")
        return False


def calculate_compression_ratio(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    ratio = compressed_size / original_size
    return original_size, compressed_size, ratio


# Example usage
if __name__ == "__main__":
    text1 = "abababababababababababababababababababababababababababababababababab"
    text2 = "this is an example for huffman and lempel-ziv encoding, which demonstrates varied character distribution."

    with open("text1.txt", "w") as f:
        f.write(text1)
    with open("text2.txt", "w") as f:
        f.write(text2)

    encoded_huffman_file1 = "encoded_huffman1.bin"
    decoded_huffman_file1 = "decoded_huffman1.txt"
    encoded_lz_file1 = "encoded_lz1.txt"
    decoded_lz_file1 = "decoded_lz1.txt"

    encoded_huffman_file2 = "encoded_huffman2.bin"
    decoded_huffman_file2 = "decoded_huffman2.txt"
    encoded_lz_file2 = "encoded_lz2.txt"
    decoded_lz_file2 = "decoded_lz2.txt"

    # Huffman encoding/decoding for text1
    encodeHuffman("text1.txt", encoded_huffman_file1)
    decodeHuffman(encoded_huffman_file1, decoded_huffman_file1)

    # Lempel-Ziv encoding/decoding for text1
    encodeLZ("text1.txt", encoded_lz_file1)
    decodeLZ(encoded_lz_file1, decoded_lz_file1)

    # Huffman encoding/decoding for text2
    encodeHuffman("text2.txt", encoded_huffman_file2)
    decodeHuffman(encoded_huffman_file2, decoded_huffman_file2)

    # Lempel-Ziv encoding/decoding for text2
    encodeLZ("text2.txt", encoded_lz_file2)
    decodeLZ(encoded_lz_file2, decoded_lz_file2)

    # Calculate compression ratios
    original_size1, compressed_size_huffman1, ratio_huffman1 = calculate_compression_ratio("text1.txt",
                                                                                           encoded_huffman_file1)
    _, compressed_size_lz1, ratio_lz1 = calculate_compression_ratio("text1.txt", encoded_lz_file1)

    original_size2, compressed_size_huffman2, ratio_huffman2 = calculate_compression_ratio("text2.txt",
                                                                                           encoded_huffman_file2)
    _, compressed_size_lz2, ratio_lz2 = calculate_compression_ratio("text2.txt", encoded_lz_file2)

    print(f"Text 1 (LZ better):\nOriginal size: {original_size1} bytes")
    print(f"Huffman compressed size: {compressed_size_huffman1} bytes, Compression ratio: {ratio_huffman1:.2f}")
    print(f"Lempel-Ziv compressed size: {compressed_size_lz1} bytes, Compression ratio: {ratio_lz1:.2f}\n")

    print(f"Text 2 (Huffman better):\nOriginal size: {original_size2} bytes")
    print(f"Huffman compressed size: {compressed_size_huffman2} bytes, Compression ratio: {ratio_huffman2:.2f}")
    print(f"Lempel-Ziv compressed size: {compressed_size_lz2} bytes, Compression ratio: {ratio_lz2:.2f}")
