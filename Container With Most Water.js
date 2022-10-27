var maxArea = function(height) {
  let i = 0;
let j = height.length-1;
let maximumArea = 0;
while(i<j){
 
  
  let area = Math.min(height[i],height[j])*(j-i);
   maximumArea = Math.max(area,maximumArea);
  if(height[i]<height[j])i++;
  else{
    j--;
  }
}
return maximumArea;
};
