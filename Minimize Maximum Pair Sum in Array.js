var minPairSum = function(nums) {
     let sum = 0;
   nums.sort((a,b) => a - b);
   
   let half = nums.length/2;
    
   
 for(let i = 0,j=nums.length-1 ;i<half&&j>=half;i++,j--){
  sum=Math.max(sum,nums[i]+nums[j])
 }
    
    return sum;
};
