// Given two strings ransomNote and magazine, return true if ransomNote can be
// constructed by using the letters from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false
// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true

// Constraints:

// 1 <= ransomNote.length, magazine.length <= 105
// ransomNote and magazine consist of lowercase English letters.
import java.util.Arrays;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] arr1 = ransomNote.toCharArray();
        char[] arr2 = magazine.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int i = 0, j = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] == arr2[j]) {
                i++;
                j++;
            } else if (arr1[i] > arr2[j]) {
                j++;
            } else {
                return false;
            }
        }
        return i == arr1.length;
    }
}
