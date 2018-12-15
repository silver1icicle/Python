# -*- coding: utf-8 -*-
class Solution:
    def twoSum_sol1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        This the linear search approach..Simple to implement but not very efficient.
        The time complexity is O(n) in worst case.
        This is a comparison based search...thus inefficient. The best we can achieve in case of a comparison based search is O(log n)
        i.e. in case of binary search..but for this..our data has to be SORTED. 
        """
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum_sol2(self, nums, target):
        """
            Approach 1: Brute Force
            The brute force approach is simple. Loop through each element X and find if there is another value that equals to target - X.
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]

    def twoSum_sol3(self, nums, target):
        """
            In this solution, we use the concept of hash maps to enable quick search.
            We store indices in the hashmap, to handle Test case III scenario.
        """
        mapD = {}
        # Create a hash table
        for i in range(len(nums)):
            rem = nums[i] % len(nums)
            if rem in mapD.keys():
                mapD[rem].append((nums[i],i))
            else:
                mapD[rem] = [(nums[i],i)]
        # Now do the actual search
        for i in nums:
            tempNumHash = i % len(nums)
            tempComplementHash = (target - i) % len(nums)
            tempKeys = mapD.keys()
            if tempComplementHash in tempKeys:
                ll = mapD[tempComplementHash]
                for j in ll:
                    if j[0] + i == target and j[1] != nums.index(i):
                        return [nums.index(i),j[1]]
                    
    def twoSum_sol4(self, nums, target):
        """
            One of the solutuons posted in the discussion forum by Nathan Fegard
            This is by far the easiest solution - Simply Super!!
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
        


if __name__ == '__main__':
    # Test case - I
    #nums = [2, 7, 11, 15]
    #target = 9

    # Test case - II
    #nums = [3,2,4]
    #target = 6

    # Test case - III
    nums = [3,3]
    target = 6
    
    '''
    obj = Solution()
    res = obj.twoSum_sol2(nums, target)
    print(res)
    '''
    obj = Solution()
    print(obj.twoSum_sol4(nums, target))
    
