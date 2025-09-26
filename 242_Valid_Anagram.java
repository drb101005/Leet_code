// Given two strings s and t, return true if t is an anagram of s, and false
// otherwise.

// Example 1:

// Input: s = "anagram", t = "nagaram"

// Output: true

// Example 2:

// Input: s = "rat", t = "car"

// Output: false

// Constraints:

// 1 <= s.length, t.length <= 5 * 104

import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        s = new String(arr1);
        t = new String(arr2);

        HashMap<Integer, String> hm1 = new HashMap<>();
        HashMap<Integer, String> hm2 = new HashMap<>();

        if (s.length() == t.length()) {
            int j = 0, k = 0, h = 0, g = 0;
            while (j < s.length() && h < t.length()) {
                hm1.put(j, String.valueOf(s.charAt(k)));
                j = j + 1;
                k = k + 1;
                hm2.put(h, String.valueOf(t.charAt(g)));
                h = h + 1;
                g = g + 1;
            }
            if (hm1.equals(hm2)){
                return true;
            }
            return false;
        } else {
            return false;
        }
    }
}
