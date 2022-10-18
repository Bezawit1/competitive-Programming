var longestSubarray = function(nums) {
        let last = 0;
       let count = 0;
     let res = 0;
    for (let i = 0; i <= nums.length; i++)
        if (nums[i]) count++
        else {
            if (last + count >res) res = last + count
            last = count, count = 0
        }
    return res === nums.length ? res - 1 : res
};
