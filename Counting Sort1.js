function countingSort(arr) {
    // Write your code here
  let counter = []
    for(var i=0;i<100;i++)
        {
            var count=0;
            for(var k=0;k<arr.length;k++)
                {
                    if(arr[k]==i)
                        {
                            count++;
                           
                        }
                }
            counter.push(count);
        }
    return counter;
}
