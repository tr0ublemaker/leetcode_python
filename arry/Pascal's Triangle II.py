k=7

nums=[1 for x in xrange(k)]
#print nums

for i in range (2,k):
    for j in range (i-1,-1,-1):

        if j==i-1:
            nums[j]=nums[j-1]+1
            #print nums
        elif j==0:
            nums[j]=1

        else:
            nums[j]=nums[j]+nums[j-1]

print nums