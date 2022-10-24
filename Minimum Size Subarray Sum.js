var minSubArrayLen = function(target, nums) {
  let sum = 0;
    let minLength = Infinity;
    let prevIndex = 0;
    
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];

        while (sum >= target) {
            minLength = Math.min(minLength, i - prevIndex + 1);
            sum -= nums[prevIndex];
            prevIndex++;
        }
    }
    
    
    return minLength === Infinity ? 0 : minLength;
}
