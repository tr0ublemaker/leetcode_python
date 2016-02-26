def plusOne(self, digits):
    add=0
    digits[len(digits)-1]+=1
    for i in range(len(digits)-1,0,-1):
        digits[i]+=add
        if digits>10:
            add=1
            digits[i]=digits[i]%10
        else:
            digits[i]=digits[i]
            add=0
    if add>0:
        for i in range(len(digits),0,-1):
            digits[i]=digits[i-1]
            if i==0:
                digits[i]=1
    return digits
