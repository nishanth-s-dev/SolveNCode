# Platform          : Lintcode
# Problem Number    : 659
# Problem Name      : Encode and Decode Strings
# Problem Topics    : String
# Problem URL       : https://www.lintcode.com/problem/659/


def string_encode(strings):
    res = ""
    for string in strings:
        res += str(len(string)) + "#" + string
    return res

def string_decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res

if __name__ == "__main__":
    strings = ["stringOne", "stringTwo", "stringThree", "stringFour", "string#9Five", "stringSeven"]
    print("Before Encoding : ", strings)
    encoded_strings = string_encode(strings)
    print("Encoded : " + encoded_strings)
    print("Decoded : " + str(string_decode(encoded_strings)))