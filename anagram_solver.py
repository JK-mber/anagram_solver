from collections import Counter


def read_words(fname):
    print('Loading file... ', end='')
    f = open(fname, 'r')
    print('done')
    return f.readlines()


def trim(x):
    return "".join(x.split())


def remove_impossible_words(words, anag_c):
    print('Removing impossible words from list... ', end='')
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
    print('done')
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
                    for wordlist in self.anagrams(anag_c - Counter(words[0]), n_words=n_words + 1):
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

    words = read_words(wordfile)
    anagram_counter = Counter(trim(anag_base))
    words = remove_impossible_words(words, anagram_counter)
    trie = Trie()

    print('Adding words to trie... ', end='')
    for word in words:
        trie.add_word(word)
    print('done')

    for anagram in trie.anagrams(anagram_counter, rootcheck=False, maxwords=4):
        print(anagram)

