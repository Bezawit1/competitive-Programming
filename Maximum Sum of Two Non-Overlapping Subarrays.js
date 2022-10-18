var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
   let len = nums.length;
    for(let i = 1; i < len; i++) {
        nums[i] += nums[i - 1];
    }
    
    let firstMax = nums[firstLen - 1], secondMax = nums[secondLen-1];
    let res = nums[secondLen + firstLen - 1];
    for(let i = firstLen + secondLen ; i< len ; i++) {
        
        firstMax = Math.max(firstMax, nums[i - secondLen ] - nums[i - secondLen- firstLen]);
       secondMax= Math.max(secondMax, nums[i - firstLen ] - nums[i - secondLen- firstLen]);
        res = Math.max(res,
            firstMax + nums[i] - nums[i - secondLen],
            secondMax + nums[i] - nums[i - firstLen]
        )
    }
    return res;
};
