import math

def calcSequence(stype,nums): #s type: harmonic,square root,
    nums = [float(x) for x in nums.split(",")]
    if stype in ["arth","arithmetic"]:
        #given start, add and end return sum, amount
        if len(nums) != 3:
            return "\x035Invalid input, use form @calc.sequence arithmetic start,adder,end"
        Sum = 0; end = nums[2]; start = nums[0]; add = nums[1]
        for i in range(0,int(end-start)):
            Sum += start + add*i
        return "Sum of arithmetic sequence " + str(start) + " + " + str(start+add) + "... is " + str(Sum)
        
    if stype in ["geo","geometric"]:
        #given start, add and end (optional) return sum, amount
        if len(nums) != 3 and len(nums) != 2:
            return "\x035Invalid input, use form @calc.sequence geometric start,multiplier,end (end is optional)"
        Sum = 0; start = nums[0]; r = nums[1]
        
        if len(nums) == 2: 
            if 1-r <= 0:
                return "The sum of the geometric sequence " + str(start) + " + " + str(start*r) + " ... is infinity"
            S = str(start / (1-r))
            return "The sum of the geometric sequence " + str(start) + " + " + str(start*r) + " ... is " + str(S)
        end = nums[2]
        return "The sum of the geometric sequence " + str(start) + " + " + str(start*r) + " ... is " + str(start*(1-r**end)/(1-r))

    if stype in ["fib","fibonacci"]:
        if len(nums) != 1:
            return "\x035Invalid input, use form @calc.sequence fib n to solve for nth term."
        answer = 1/math.sqrt(5) * ( ((1+math.sqrt(5))/2)**nums[0] - ((1-math.sqrt(5))/2)**nums[0] )
        return "The " + str(nums[0]) + "th term of the fibonacci sequence is " + str(round(answer))
        
    if stype == "sumsquare":
        if len(nums) != 1:
            return "\x035Invalid input, use form @calc.sequence sumsquare n to calculate 1^2 + 2^2 ... n^2."
        n = nums[0]
        return "The sum 1^2 + 2^2 ... + " + str(nums[0]) + "^2 = " + str(n*(2*n+1)*(n+1) / 6)
        
