var smallerNumbersThanCurrent = function(nums) {
    var count = 0 ;
    var res = [];
    for(let i = 0 ; i<nums.length ; i++){
for(let j = 0 ; j<nums.length ; j++){
    if(nums[j]<nums[i]&&j!=i){
       count++;
}
}
res.push(count);
  count=0;      
        

    }
    return res;
};
