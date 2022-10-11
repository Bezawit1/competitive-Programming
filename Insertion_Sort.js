function insertionSort1(n, arr) {
    // Write your code here
    var last = arr[n-1];
   while (arr[--n - 1] >last) {
    arr[n] = arr[n - 1];

    console.log(...arr);
  }
arr[n] = last;
console.log(...arr)

}
