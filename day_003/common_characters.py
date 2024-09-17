# Platform          : AlgoExpert
# Problem Name      : Common Characters
# Difficulty        : Easy
# Category          : Arrays, Hashmap
# Problem URL       : https://www.algoexpert.io/questions/common-characters

def commonCharacters(strings):
    res = []
    hmap = {}

    for string in strings:
        set_string = set(string)
        for letter in set_string:
            hmap[letter] = hmap.get(letter, 0) + 1

    for key, value in hmap.items():
        if value == len(strings):
            res.append(key)

    return res

if __name__ == '__main__':
    print(commonCharacters(['abc', 'bca', 'bcd', 'dbc', 'bce', 'fbc', 'gbc', 'hbc']))