function countSwaps(a) {
    // Write your code here
   var swaps=0;  
for(var i = 0; i < a.length; i++){
    
  
   for(var j = 0; j < ( a.length - i -1 ); j++){
      
     if(a[j] > a[j+1]){
        var temp = a[j]
       a[j] = a[j + 1]
       a[j+1] = temp
       swaps++;
     }
   }
 }
 // Print the sorted aay
 console.log("Array is sorted in " + swaps+" swaps.");
 console.log("First Element: " +a[0]);
 console.log("Last Element: " + a[a.length-1]);
}
