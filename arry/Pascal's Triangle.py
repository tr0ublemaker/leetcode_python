for i in range(numRows):
    son=[]
    nums.append(son)
    length=len(nums[i])
    nums[i][0]=nums[i][length-1]=1
    for j in range(1,numRows-1):
        nums[i][j]=nums[i-1][j-1]+nums[i-1][j]