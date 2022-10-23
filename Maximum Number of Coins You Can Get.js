var maxCoins = function(piles) {
 piles.sort((a, b) => b - a);
    
    let sum = 0,
	    startindex = 1,
		endIndex= 2 * piles.length / 3;
    while (startindex  < endIndex) {
        sum += piles[startindex];
        startindex += 2;
    }
    return sum ;
};
