'''
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

 

示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
示例 2：

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
'''

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        if not s:
            return s

        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i, j =0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1

            if j == len(word):
                return word

        return ""
