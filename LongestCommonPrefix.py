class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = "" # start with the empty string 
        for i in range(len(strs[0])): # runs for the length of the first string in the array
        #doesnt really matter what we choose becaause as soon as one ends the other will to
            for s in strs: # for each string in the list strs 
                if i == len(s) or s[i] != strs [0][i]: # goes character by character across all the string. Checking if they are not equal. This also ends if a string is too short.
                    return ans 
            ans += strs[0][i] # builds onto the string

        return ans