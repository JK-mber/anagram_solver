'''
Computes possible anagrams using a loaded list of words
'''

from collections import Counter

anag_base = 'poultry outwits ants'
wordfile = 'wordlist'

def read_words(fname):
    f = open(fname,'r')
    print('File loaded')
    return f.readlines()


def trim(x):
    return "".join(x.split())

def remove_impossible_words(words, anag_c):
    i = 0
    while i < len(words):
        words[i] = trim(words[i])
        word_c = Counter(words[i])
        if not all(x in anag_c for x in word_c):
            words.pop(i)
        else:
            i += 1
    print('Impossible words removed')


def anagram_generator(words, anag_c, root_check=False):
    l_words = words[:]  # local copy
    i = 0
    while i < len(l_words):
        word = l_words[i]
        if root_check:
            print('Checking descendants of ' + word)
        word_c = Counter(word)
        if all(letter in anag_c for letter in word_c):  # Found a matching word
            if anag_c == word_c:
                yield [word]
            elif anag_c - word_c:
                for res in anagram_generator(l_words, anag_c-word_c):
                    # if res is True:  # end of recursion reached (no more letters in anagram)
                    #     yield [word]
                    # if res:  # sequence found
                    yield [word] + res

        l_words.pop(0)
        if root_check:
            print('Words left: ' + str(len(l_words)))
        else:
            i += 1


def is_anag(s1, s2):
    return Counter(s1) == Counter(''.join(s2))



words = read_words(wordfile)
# words[0] = 'poultryoutwits'
# words[1] = 'ants'
anag_c = Counter(trim(anag_base))

remove_impossible_words(words, anag_base)  # words is a list (mutable type)
words = list(set(words))
print(len(words))
words.sort()
print(words)

for a in anagram_generator(words, anag_c, True):
    print(is_anag(trim(anag_base), a))
    print(a)
#
# print('done')






































