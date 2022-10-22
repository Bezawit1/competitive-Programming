var maxFrequency = function(nums,k) {

  nums.sort(function(a,b){return b-a});
    let j=0;
let prev=0;
  let max=0;
    for(let i=0;i<nums.length;i++){
        
        while(j<nums.length && nums[i]-nums[j]<=k){
            k -= (nums[i]-nums[j]);
           
            max = Math.max(max,j-i+1);
            prev=j;
            j++;
        }
       
        if(i<nums.length-1){
            k += (nums[i]-nums[i+1])*(prev-i);
        }
    }
    return max;


};
