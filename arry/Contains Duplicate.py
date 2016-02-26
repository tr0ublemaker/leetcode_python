class Solution(object):
    def containsDuplicate(self, nums):
        t=set([])  #使用set不可重复属性
        resualt=False
        length=len(t);
        for item in nums:
            t.add(item)
            if len(t)>length:
                length=len(t)
            else:
                resualt=True
        return resualt

        """
        :type nums: List[int]
        :rtype: bool
        """