class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            curr_trie = trie
            for char in word:
                char_index = ord(char) - ord("a")
                if curr_trie.children[char_index] is None:
                    curr_trie.children[char_index] = Trie()
                    curr_trie = curr_trie.children[char_index]
                else:
                    curr_trie = curr_trie.children[char_index]
            curr_trie.is_end_of_word = True

        curr_trie = trie
        curr_prefix = ""
        while True:
            children = [
                (i, c) for i, c in enumerate(curr_trie.children) if c is not None
            ]
            if len(children) != 1 or curr_trie.is_end_of_word:
                break
            else:
                idx, child = children[0]
                curr_trie = child
                curr_prefix += chr(idx + ord("a"))
            
        return curr_prefix

def main(words, want):
    s = Solution()
    res = s.longestCommonPrefix(words)
    if res != want:
        print("mismatch wanted {} and got {}".format(want, res))

if __name__ == "__main__":
    tests = [
        [["flower","flow","flight"], "fl"],
        [["dog","racecar","car"], ""],
    ]
    for test in tests:
        main(test[0], test[1])
