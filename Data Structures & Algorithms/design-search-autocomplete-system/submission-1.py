class TrieNode:
    def __init__(self):
        self.children = {}
        # Only store the top 3 (count, sentence) pairs for this prefix
        self.hot_list = []

class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.sentence_counts = {}
        self.current_query = ""
        
        for s, t in zip(sentences, times):
            self.sentence_counts[s] = t
            self._insert(s)

    def _insert(self, sentence):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            self._update_hot_list(node, sentence)

    def _update_hot_list(self, node, sentence):
        # Remove the sentence if it already exists in the hot_list
        new_list = [item for item in node.hot_list if item[1] != sentence]
        # Add current sentence with its updated frequency
        new_list.append((-self.sentence_counts[sentence], sentence))
        # Sort and keep only top 3
        new_list.sort()
        node.hot_list = new_list[:3]

    def input(self, c: str) -> list[str]:
        if c == "#":
            self.sentence_counts[self.current_query] = \
                self.sentence_counts.get(self.current_query, 0) + 1
            self._insert(self.current_query)
            self.current_query = ""
            self.curr_pointer = self.root # Reset pointer
            return []

        if self.current_query == "":
            self.curr_pointer = self.root
            
        self.current_query += c
        
        if self.curr_pointer and c in self.curr_pointer.children:
            self.curr_pointer = self.curr_pointer.children[c]
            return [item[1] for item in self.curr_pointer.hot_list]
        else:
            self.curr_pointer = None
            return []