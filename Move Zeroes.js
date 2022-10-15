var moveZeroes = function(nums) {
 
 
  for(let i = 0 ; i<nums.length-1 ; i++){
 for(let j = i+1 ; j<nums.length;j++){
      if(nums[i]==0&&nums[j]!=0){
         var temp = nums[i];
          nums[i] = nums[j]
          nums[j]=temp;
         break;
      }
 }  
  }
 return nums;
};
