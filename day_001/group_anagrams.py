# Platform          : Leetcode
# Problem Number    : 49
# Problem Name      : Group Anagrams
# Problem Topics    : Array, Hashtable, Sorting, String
# Problem URL       : https://leetcode.com/problems/group-anagrams/


from collections import defaultdict


def group_anagrams(words):
    res = defaultdict(list)
    for word in words:
        counter = [0] * 26
        for letter in word:
            counter[ord(letter) - ord('a')] += 1
        res[tuple(counter)].append(word)
    return list(res.values())

if __name__ == '__main__':
    words_list = ["act","pots","tops","cat","stop","hat"]
    print(group_anagrams(words_list))