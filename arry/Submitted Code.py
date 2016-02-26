class Solution(object):
    def summaryRanges(self, nums):
        length=len(nums)
        strs=[]
        if length==0:
            return strs
        else:
            minNum=maxNum=nums[0]
            for i in range(length):
                if i==length-1:
                        maxNum=nums[i]
                        if minNum==maxNum:
                            strs.append(str(minNum))
                        else:
                            strs.append(str(minNum)+'->'+str(maxNum))
                else:
                    if nums[i]+1!=nums[i+1]:
                        maxNum=nums[i]
                        if minNum==maxNum:
                            strs.append(str(minNum))
                        else:
                            strs.append(str(minNum)+'->'+str(maxNum))
                        minNum=nums[i+1]
            return strs




        """
        :type nums: List[int]
        :rtype: List[str]
        """