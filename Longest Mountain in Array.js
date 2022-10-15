var longestMountain = function(arr) {
let max = 0 ;
    for(let i = 0 ; i<arr.length ; i++){
let j = i
while(arr[j]<arr[j+1]){
j++;

}
    const k= j
        while(j>i&&arr[j]>arr[j+1]){

        j++;
        }
        if(j>k&&k>i){
            max = Math.max(max,j-i+1)
             i=j
            i--
            
            }
        }
    
    
return max;
};
