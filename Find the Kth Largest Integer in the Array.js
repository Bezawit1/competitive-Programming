var kthLargestNumber = function(nums, k) {
  let sorted = nums.map(x=>BigInt(x)).sort((a,b)=>a>=b?-1:1);
    return sorted[k-1].toString();


    
    
};
