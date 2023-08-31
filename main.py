class Solution:
    def longestPalindrome(self, s: str) -> str:
        dict_palin = {}
        if len(s)==1:
            return s
        else:
            for i in range(len(s)-1):
                for j in range(i+1,len(s)+1):
                    original = s[i:j] 
                    reverse = original[::-1]
                    if original==reverse:
                        dict_palin[original]=len(original)
        sorted_dict = sorted(dict_palin.items(), key=lambda x: x[1])
        return sorted_dict[-1][0]

palindrom_obj = Solution()
palindrom_obj.longestPalindrome("adhbahhhahahahhhj")