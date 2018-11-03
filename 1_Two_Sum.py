class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        hashmap1 = {}
        for i in range(length):
            # build the hashmap first
            hashmap1[nums[i]] = i
        for i in range(length):
            # calculate the value we are looking for
            look_up = target - nums[i]
            # get the value's index
            j = hashmap1.get(look_up, None)
            # value exist and not use the same item twice
            if j != None and j != i:
                # we can return our result or we should continue to loop
                return [i, j]