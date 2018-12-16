# can not understand the code
from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        if not words:
            return []
        # the class map: element: the number of occurrences
        counter = Counter(words)
        # each given word have the same length
        unit = len(words[0])
        ans = []
        # the window is the sum length of each loop
        window = unit * len(words)

        for margin in range(unit):
            sub_counter = Counter()
            score = 0
            # take three character from the string each time
            # the margin is take from the range(unit) which make sense due to unit+1 is the same as 1
            # calculate just one window as the following loop
            for cur in range(margin, margin+window, unit):
                word = s[cur:cur+unit]
                if word in counter:
                    sub_counter[word] += 1
                    if sub_counter[word] <= counter[word]:
                        score += 1

            if score == len(words):
                ans.append(margin)

            for start in range(margin, len(s), unit):
                removed_word = s[start:start+unit]
                if removed_word in counter:
                    sub_counter[removed_word] -= 1
                    if sub_counter[removed_word] < counter[removed_word]:
                        score -= 1

                added_word = s[start+window: start+window+unit]
                if added_word in counter:
                    sub_counter[added_word] += 1
                    if sub_counter[added_word] <= counter[added_word]:
                        score += 1
                if score == len(words):
                    ans.append(start+unit)
        return ans
s=Solution()
print(s.findSubstring("barfoothefoobarman",["foo","bar"]))