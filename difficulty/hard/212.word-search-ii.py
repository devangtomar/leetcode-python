from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j):
            char = board[i][j]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.is_end_of_word:
                result.add(next_node.word)

            board[i][j] = "#"  # Mark the cell as visited
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (
                    0 <= x < len(board)
                    and 0 <= y < len(board[0])
                    and board[x][y] != "#"
                ):
                    dfs(next_node, x, y)
            board[i][j] = char  # Unmark the cell

        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j)

        return list(result)
