# anagram_solver
Finds possible anagrams

Built to solve the [trustpilot code challenge](https://followthewhiterabbit.trustpilot.com/cs/step3.html) (finding an anagram with a certain md5 hash)

# Structure
It is built by first indexing all words in a alphbetically sorted letter-trie structure, where word-anagrams are grouped together. This means that e.g. owl and low are both stored under l-o-w. By using this approach, the algorithm can group the resulting word-anagrams, reducing the required iterations. Additionally, the trie structure greatly optimizes the anagram search.

With max 3 words, it takes less than half a minute to find all anagrams (791 unique combinations of words, 791\*3!=4746 anagrams). When these are found, it's just about looping through the anagrams checking the md5 digest, comparing it with the target digest. With max 4 words, it takes a bit longer (5-10 minutes) - and finds 370255 unique combinations of words. 
