# Platform          : Leetcode
# Problem Number    : 20
# Problem Name      : Valid Parentheses
# Problem Topics    : Stack, String
# Problem URL       : https://leetcode.com/problems/valid-parentheses


def valid_parentheses(string):
    pairs = {'}' : '{', ']' : '[', ')' : '('}

    stack = []

    for letter in string:
        if letter in pairs.keys():
            if stack and pairs[letter] != stack.pop():
                return False
        else:
            stack.append(letter)

    return not stack

if __name__ == '__main__':
    print(valid_parentheses("()[]{}"))