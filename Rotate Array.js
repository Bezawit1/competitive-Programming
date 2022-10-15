var rotate = function(nums, k) {


    k = (k % nums.length)
    
    let result= nums.splice(nums.length - k)

    nums.splice(0,0,...result)
};
