# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        # Count characters in chars
        count = {}
        for ch in chars:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        answer = 0

        # Check every word
        for word in words:

            # Count characters in current word
            count2 = {}
            for ch in word:
                if ch in count2:
                    count2[ch] += 1
                else:
                    count2[ch] = 1

            # Compare both dictionaries
            good = True

            for ch in count2:
                if ch not in count:
                    good = False
                    break

                if count2[ch] > count[ch]:
                    good = False
                    break

            if good:
                answer += len(word)

        return answer