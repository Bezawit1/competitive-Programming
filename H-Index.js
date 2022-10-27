var hIndex = function(citations) {
  citations.sort(function(a,b){return b-a});
    let count = 0;
    for(let i = 0 ; i<citations.length;i++){
if(citations[i]-count>0)count++;
        else{
            return count
        }
   
   
   }
  return count
};
