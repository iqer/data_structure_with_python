class Solution:

    # def isValid(self, s: str) -> bool:
    #     array = list()
    #     match_map = {
    #         '[': ']',
    #         '{': '}',
    #         '(': ')',
    #     }
    #     for i in range(len(s)):
    #         if s[i] in match_map.keys():
    #             array.append(s[i])
    #         elif s[i] in match_map.values():
    #             if array and (s[i] == match_map.get(array[-1])):
    #                 array.pop()
    #             else:
    #                 return False
    #     if array:
    #         return False
    #     else:
    #         return True
    def isValid(self, s: str) -> bool:

        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


if __name__ == "__main__":
    s1 = Solution()
    print(s1.isValid('[()]'))
