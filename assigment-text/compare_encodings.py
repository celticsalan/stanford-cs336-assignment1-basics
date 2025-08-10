def compare_encodings(text):
    """
    Encodes a given string into UTF-8, UTF-16, and UTF-32 byte sequences
    and prints the results for comparison.

    Args:
        text (str): The input string to encode.
    """
    print(f"Original string: '{text}'")

    # UTF-8 encoding
    utf8_encoded = text.encode("utf-8")
    print(f"UTF-8 encoded: {utf8_encoded} (Length: {len(utf8_encoded)} bytes)")

    # UTF-16 encoding (with default 'utf-16' which includes BOM)
    utf16_encoded = text.encode("utf-16")
    print(f"UTF-16 encoded: {utf16_encoded} (Length: {len(utf16_encoded)} bytes)")

    # UTF-32 encoding (with default 'utf-32' which includes BOM)
    utf32_encoded = text.encode("utf-32")
    print(f"UTF-32 encoded: {utf32_encoded} (Length: {len(utf32_encoded)} bytes)")

    print("-" * 30)

# Example usage:
compare_encodings("Hello")
compare_encodings("你好")  # Chinese characters
compare_encodings("😀")   # Emoji character
compare_encodings("München") # German city name with umlaut