# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

import zlib

def string_to_bytes(input_string):
    try:
        encoded_bytes = input_string.encode("utf-8")
        return encoded_bytes
    except Exception as e:
        print("Error:", e)
        return None

def compress_bytes(byte_obj):
    compressed_bytes = zlib.compress(byte_obj)
    return compressed_bytes

def decompress_bytes(compressed_byte_obj):
    decompressed_bytes = zlib.decompress(compressed_byte_obj)
    return decompressed_bytes

def main():
    try:
        original_string = input("Please enter a string: ")
        byte_ver = string_to_bytes(original_string)

        compressed_string = compress_bytes(byte_ver)
        decompressed_string = decompress_bytes(compressed_string)

        print("\nOriginal Bytes:", original_string)
        print("\nConverted to Bytes:", byte_ver)
        print("\nCompressed Bytes:", compressed_string)
        print("\nDecompressed Bytes:", decompressed_string)
        print("\nDecompressed String:", decompressed_string.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
