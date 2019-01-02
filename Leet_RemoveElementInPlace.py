'''
Problem Statement: Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example 1:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
'''



class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while(1):
            try:
                nums.remove(val)                        # Deletes the first occurence of the element found within the list
            except ValueError:                          # Trying to delete an element which is not present in the list results in <ValueError>
                return (len(nums))                      # We return only the len of the list

if __name__ == '__main__':
    obj=Solution()
    nums = [3,2,2,3]
    val = 3
    print(obj.removeElement(nums, val))
    print(nums)      # List is a mutable DS + values are passed by reference rather passed by object in Python
                     # Therefore changes made in a list in the function are replicated in the main calling function aswell   
