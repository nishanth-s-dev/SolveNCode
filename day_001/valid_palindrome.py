# Platform          : Leetcode
# Problem Number    : 125
# Problem Name      : Valid Palindrome
# Problem Topics    : Two Pointer, String
# Problem URL       : https://leetcode.com/problems/valid-palindrome/


def is_palindrome(s):
    s = "".join([char.lower() for char in s if is_alpha_num(char.lower())])
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


def is_alpha_num(char):
    return ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')

if __name__ == "__main__":
    string = input()
    print(is_palindrome(string))