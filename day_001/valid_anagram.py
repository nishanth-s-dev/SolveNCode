# Platform          : Leetcode
# Problem Number    : 242
# Problem Name      : Valid Anagram
# Problem Topics    : String, Hashtable, Sorting
# Problem URL       : https://leetcode.com/problems/valid-anagram/


from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

if __name__ == '__main__':
    word_one = input("Enter a first word: ")
    word_two = input("Enter a second word: ")
    print(is_anagram(word_one, word_two))