class Solution(object):
    def rotate(self, nums, k):
        _num=list(nums)
        length=len(nums)
        for i in range(length):
            nums[i]=_num[(i+k)%length]
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
