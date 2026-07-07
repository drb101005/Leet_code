# // Given two strings ransomNote and magazine, return true if ransomNote can be
# // constructed by using the letters from magazine and false otherwise.

# // Each letter in magazine can only be used once in ransomNote.

# // Example 1:

# // Input: ransomNote = "a", magazine = "b"
# // Output: false
# // Example 2:

# // Input: ransomNote = "aa", magazine = "ab"
# // Output: false
# // Example 3:

# // Input: ransomNote = "aa", magazine = "aab"
# // Output: true

# // Constraints:

# // 1 <= ransomNote.length, magazine.length <= 105
# // ransomNote and magazine consist of lowercase English letters.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_r = {}
        count_m = {}
        #counting chars in ransomNote
        for r in ransomNote:
            if r in count_r:
                count_r[r] += 1
            else:
                count_r[r] = 1
        #counting chars in magazine
        for m in magazine:
            if m in count_m:
                count_m[m] += 1
            else:
                count_m[m] = 1
        for ch in count_r:
            if ch not in count_m:
                return False

            if count_r[ch] > count_m[ch]:
                return False


        return True