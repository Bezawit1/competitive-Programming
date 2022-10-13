var carPooling = function(trips, capacity) {
 trips.sort((a, b) => a[1] - b[1])
   
        trip = Array(1000).fill(0)
    
    for(let i = 0; i < trips.length; i++) {
        for(let j = trips[i][1]; j < trips[i][2]; j++) {
            trip[j] += trips[i][0]
            if(trip[j] > capacity) return false;
        }
    }
    return true;
};
