var minPairSum = function(nums) {
     let sum = 0;
   nums.sort((a,b) => a - b);
   
   let half = nums.length/2;
    
    for (let i = 0; i < half; i++) {
       sum = Math.max(sum, nums[i] + nums[nums.length - i - 1])
    }
    
    return sum;
};
