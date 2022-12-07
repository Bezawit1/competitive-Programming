var minIncrementForUnique = function(nums) {
    let count = 0;
    nums.sort((a,b)=>a-b)
    for(let i = 1; i < nums.length; i++) {
        while(nums[i] <= nums[i - 1]) {
            nums[i] ++
            count ++
        }
    }
    
    
    return count;
};
