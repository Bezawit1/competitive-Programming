var productExceptSelf = function(nums) {
    var product = 1 ;
    var answer = [];
    for(let i = 0 ; i < nums.length ; ){
for(let j = 0 ; j< nums.length ; j++){
if(i == j){
continue;
}
else{
product*=nums[j];

}
}
 answer.push(product);
i++;
        product =1;
 }
  return answer;
};
