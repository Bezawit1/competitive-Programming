function countingValleys(steps, path) {
    // Write your code here
    var arr = path.split("");
 
    var top= 0;
    var low= 0;
    for(var i =0; i < steps;i++) {
        if(arr[i] == "U") {
           top++;
            
        } else if(arr[i] == "D") {
            
           top--;
            if(top == -1) {
                low++;
            }
        }
    }
   return(low);
}
