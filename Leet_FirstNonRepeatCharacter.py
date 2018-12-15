# -*- coding: cp1252 -*-    # Added by the IDE..helps in identifying special Non-ASCII characters in the file
"""
    Objective    : To find the first non repeating character in the string
    Strategy     : Use OrderedDict DS in Python
    Introduction : This "collections "module implements specialized container datatypes providing alternatives
                  to Python’s general purpose built-in containers, dict, list, set, and tuple.
"""
import collections

class Solution:
    def firstUniqChar(self, testStr):
        # Create a hash map by traversing the string and recording the number of times each character appears in the string
        # Time Complexity: O(n)
        d = collections.OrderedDict()
        for i in testStr:
            print i
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1

        # Next we use that hashmap as a reference to return the index of the unique character
        for i in d.keys():
            if d[i] == 1:
                return testStr.index(i)
        return None


if __name__ == '__main__':
    testStr = "LoveLeetCode"
    obj = Solution()
    print "The index of the first Non Repeating character in the string:----->",obj.firstUniqChar(testStr)
