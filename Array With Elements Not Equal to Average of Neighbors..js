var rearrangeArray = function(nums) {
 nums.sort((a, b) => a-b); 
  let result = [];
  let i = 0;
  let j= nums.length-1;  
  while(i < j){
    result.push(nums[i++]);
    result.push(nums[j--]);
  }  
  if(i == j) result.push(nums[i]);   
  return result;
};
