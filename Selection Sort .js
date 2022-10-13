class Solution
{
  
  selectionSort(arr, n) {
    function swap(arr,a, b)
{
    var temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
      
   var i, j, min;
 
    
    for (i = 0; i < n-1; i++)
    {
          min = i;
        for (j = i + 1; j < n; j++)
        if (arr[j] < arr[min])
            min = j;
 
      
        swap(arr,min, i);
        
    }
   
    return arr;
  
    }
  
    //Function to sort the array using selection sort algorithm.
    select(arr, n) {
      let min = arr[0];
      
      for (let i = 0; i < arr.length; i++) {
        if (min > arr[i + 1]) {
          min = arr[i + 1];
        }
      }
      let temp = arr[0];
      let index = arr.indexOf(min);
      arr[0] = min;
      arr[index] = temp;
      return arr;
    }
    
}
