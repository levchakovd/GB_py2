# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование
# https://stepik.org/lesson/21300/step/2

def compress(data):
    compressed_data = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data.append((data[i - 1], count))
            count = 1
    compressed_data.append((data[-1], count))
    return compressed_data

def decompress(compressed_data):
    data = []
    for char, count in compressed_data:
        data.extend([char] * count)
    return ''.join(data)

data = "aaaabbbcccccddddd"
compressed_data = compress(data)
print(compressed_data)
# Output: [('a', 4), ('b', 3), ('c', 5), ('d', 5)]

decompressed_data = decompress(compressed_data)
print(decompressed_data)
# Output: "aaaabbbcccccddddd"
