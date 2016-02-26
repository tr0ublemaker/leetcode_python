class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict ={}


        for i in range(len(nums)):
            if dict.get(nums[i],-1):
                j=dict.get(nums[i])
                if i-j<=k:
                    return True
            dict[nums[i]]=i
        return False
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                j = d[nums[i]]
                if i-j<=k:
                    return True
            d[nums[i]] = i
        return False