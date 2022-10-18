var numOfSubarrays = function(arr, k, threshold) {
    
    let count = 0;
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i + 1 < k) continue;
        if (sum / k >= threshold) {
            count += 1;
        };
        sum -= arr[1 + i - k];
    };
    return count;
    
};
