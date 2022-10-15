var nextGreaterElement = function(nums1, nums2) {
  var res = [];
 
  for(let i of nums1){
       var found = false
      const idx = nums2.indexOf(i)
      for(let j = idx+1 ; j<nums2.length ; j++){
if(nums2[j]>i){
res.push(nums2[j])
found =true;
    break;
}
      }
     if(!found)res.push(-1)
   
  }
 return res;
};
