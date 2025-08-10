
Unicode是一个字符集，为世界上几乎所有语言和符号提供了唯一的数字标识。

unicode1
1. unicode charactor of chr(0) '\x00' \x is an escape sequence used in many programming languages (like Python, C, PHP) to represent a byte by its hexadecimal value. 00 is the hexadecimal representation of the decimal number 0. Therefore, \x00 signifies a byte with the value 0.
2. '\x00'.__str__(): Returns '\x00'. This is a direct representation of the null character itself, which is what a user would likely expect when printing or converting the character to a string.
'\x00'.__repr__(): Returns "'\\x00'". The output includes quotes and the explicit escape sequence \\x00 (which is itself escaped to \\\\x00 to be correctly represented in the printed string). This is done for unambiguity and to ensure the string can be recreated. If \0 were used for the null character, and it was followed by a digit (e.g. \01), it could be mistakenly interpreted as a single octal escape sequence, leading to errors or confusion during reconstruction. 
3. 

计算机存储数据需要以字节 (Byte) 的形式进行，每个字节是一个8位的二进制数 (0-255)。
为了在计算机中存储或传输Unicode字符，我们需要将它们的码点转换成字节序列。
这个转换过程被称为编码 (Encoding)
UTF-8是一种广泛使用的Unicode编码方式，它将Unicode码点转换为1到4个字节的序列
: 在某些上下文中，你可能会看到以 \x 开头的字符串，后面跟着十六进制数字，这表示一个字节的十六进制值

字符 	Unicode 码点 (十六进制)	UTF-8编码 (十六进制字节序列)
W	U+0057	57
é	U+00E9	C3 A9
中	U+4E2D	E4 B8 AD

Python functions
encode() 
--- to transform a Unicode string into a bytes object, applying a chosen character encoding like UTF-8, ASCII, or Latin-1.
Input: Takes a string object as the input.
Output: Returns a new bytes object.

bytes()
--- creating bytes objects from various sources

bytes_from_constructor = bytes(my_string, "utf-8")
null_bytes = bytes(5) # Creates a bytes object of length 5, all zeros
list_of_bytes = [72, 101, 108, 108, 111] # ASCII codes for "Hello"

unicode2
1. UTF-8 uses a variable number of bytes (1 to 4) to represent Unicode characters. It encodes common ASCII characters (like English letters and numbers) using a single byte, while more complex characters (like those in Asian languages or emojis) require more bytes. This makes it more efficient than fixed-length encodings like UTF-32 (which uses 4 bytes per character) for Western languages that frequently use ASCII characters.
2. conter_examples: 'I am so good, 中文' -> UTF-8 is a variable-length encoding. Characters outside the ASCII range (0-127) are represented by multiple bytes.
