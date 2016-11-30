from hashlib import md5
from collections import Counter
from itertools import permutations


def read_words(fname):
    print('Loading file... ')
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    return lines


def trim(x):
    return "".join(x.split())


def save_to_file(fname, anagram_list):
    f = open(fname, 'w')
    for anagram in anagram_list:
        f.write(' '.join(anagram) + '\n')
    f.close()


def remove_impossible_words(words, anag_c):
    print('Removing impossible words from list... ')
    """ Removes words which include letters not in the anagram base """
    i = 0
    while i < len(words):
        words[i] = trim(words[i])
        word_c = Counter(words[i])
        if not all(x in anag_c for x in word_c):
            words.pop(i)
        else:
            i += 1
    words = sorted(list(set(words)))
    return words


class Node:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        node = self.root
        letters = sorted(trim(word))
        for l in letters:
            if l not in node.children:
                node.children[l] = Node()
            node = node.children[l]
        node.words.append(word)

    def anagrams(self, anag_c, maxwords=3, n_words=0, rootcheck=False):
        critical_letter = sorted(anag_c)[0]
        if critical_letter in self.root.children and n_words < maxwords:
            for words in self.possible_words(anag_c - Counter(critical_letter),
                                            self.root.children[critical_letter]):
                if rootcheck:
                    print('Checking descendants of word ' + str(words))
                if anag_c == Counter(words[0]):
                    for word in words:
                        yield (word,)
                else:
                    for wordlist in self.anagrams(anag_c - Counter(words[0]), n_words=n_words + 1, maxwords=maxwords):
                        for word in words:
                            yield (word,) + wordlist


    def possible_words(self, anag_c, node):
        ''' Yields all possible words in the trie structure under node given anag_c constrains '''
        # for word in node.words:
        #     yield word
        if len(node.words) > 0:
            yield tuple(node.words)
        for letter in anag_c:
            if letter in node.children:
                for words in self.possible_words(anag_c - Counter(letter), node.children[letter]):
                    yield tuple(words)

print(__name__)
if __name__ == '__main__':
    anag_base = 'poultry outwits ants'
    wordfile = 'wordlist'
    maxwords = 4
    target_hash = '4624d200580677270a54ccff86b9610e'

    anagrams = []
    try:
        f = open('anagrams_maxwords' + str(maxwords))
        for line in f:
            anagrams.append(tuple(line.strip().split(' ')))
        print('Found anagrams from file: ' + str(len(anagrams)))
    except FileNotFoundError:

        words = read_words(wordfile)
        anagram_counter = Counter(trim(anag_base))
        words = remove_impossible_words(words, anagram_counter)
        trie = Trie()

        print('Adding words to trie... ')
        for word in words:
            trie.add_word(word)
        print('Finding anagrams by iteration... ')
        for anagram in trie.anagrams(anagram_counter, rootcheck=False, maxwords=maxwords):
            anagrams.append(anagram)
        print('Number of anagrams found: ' + str(len(anagrams)))
        print('Saving anagrams to file...')
        save_to_file('anagrams_maxwords' + str(maxwords), anagrams)

    print('Checking hash of all permutations of anagrams...')
    for wordtup in anagrams:
        for anagtup in permutations(wordtup):
            anagram = ' '.join(anagtup)
            anagram_hash = md5(anagram.encode()).hexdigest()
            if anagram_hash == target_hash:
                print('Target anagram found: ' + anagram)
