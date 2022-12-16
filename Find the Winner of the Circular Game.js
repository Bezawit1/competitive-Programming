var findTheWinner = function(n, k) {
     let winner = 0;
  let arr = [];
  for(let i=1; i<=n; i++){
      arr.push(i);
  }
  
  let index = 0;
  while(arr.length > 1){ 
      let loser = index + k - 1;
      while(loser >= arr.length){
          loser -= arr.length;
      }
     
      arr.splice(loser, 1);
     
      index = loser;
      if(index >= arr.length){
          index -= arr.length;
      }
  }

 winner = arr[0];
  return winner;
};
