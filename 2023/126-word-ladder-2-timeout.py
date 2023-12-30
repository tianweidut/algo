class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        import string
        import sys
        
        self.all_trans = defaultdict(list)
        self.min_tran_len = sys.maxsize

        def backtrack(forward, state, choices):
            if forward == beginWord:
                self.min_tran_len = min(self.min_tran_len, len(state))
                self.all_trans[len(state)].append(state[::-1])
                return

            for idx in range(0, len(forward)):
                for ch in string.ascii_lowercase:
                    if ch == forward[idx]:
                        continue

                    changed_word = forward[:idx] + ch + forward[idx + 1:]
                    if changed_word == beginWord:
                        backtrack(changed_word, state + [changed_word] ,choices)
                        return

                    if not choices.get(changed_word, False):
                        continue
                    
                    if len(state) + 1 > self.min_tran_len:
                        return

                    choices[changed_word] = False
                    state.append(changed_word)
                    backtrack(changed_word, state, choices)
                    state.pop()
                    choices[changed_word] = True

        word_choices = {w: True for w in wordList}
        if endWord not in word_choices:
            return []

        backtrack(forward=endWord, state=[endWord], choices=word_choices)
        return self.all_trans[min(self.all_trans)] if self.all_trans else []        

    def findLaddersForward(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        import string
        import sys
        
        self.all_trans = defaultdict(list)
        self.min_tran_len = sys.maxsize

        # 只用DFS会超时
        def backtrack(begin, state, choices):
            if begin == endWord:
                self.min_tran_len = min(self.min_tran_len, len(state))
                self.all_trans[len(state)].append(state.copy())
                return

            for idx in range(0, len(begin)):
                for ch in string.ascii_lowercase:
                    if ch == begin[idx]:
                        continue

                    changed_word = begin[:idx] + ch + begin[idx + 1:]
                    if not choices.get(changed_word, False):
                        continue
                    
                    if len(state) + 1 > self.min_tran_len:
                        return

                    choices[changed_word] = False
                    state.append(changed_word)
                    backtrack(changed_word, state, choices)
                    state.pop()
                    choices[changed_word] = True

        word_choices = {w: True for w in wordList}
        backtrack(begin=beginWord, state=[beginWord], choices=word_choices)

        return self.all_trans[min(self.all_trans)] if self.all_trans else []

