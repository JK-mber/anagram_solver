# anagram_solver
Finds possible anagrams

Built to solve the trustpilot code challenge (finding an anagram with a certain md5 hash)

# Structure
It is built using the first indexing all words in a alphbetically sorted letter-trie structure, where word-anagrams are grouped together. This means that e.g. owl and low are both stored under l-o-w. By using this approach, the algorithm can group the resulting word-anagrams, reducing the required iterations. Additionally, the trie structure greatly optimizes the anagram search.

