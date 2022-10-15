var numRescueBoats = function(people, limit) {
  let countBoat=0;
      let i = 0;
    let j = people.length-1
    
    people.sort(function(a,b){
        return (a-b) });
   
    while(i<=j){
        if(people[i]+people[j]<=limit){
           countBoat++;
            i++;
            j--;
        }
        else{
            countBoat++;
            j--;
        }
    }
    return countBoat;
};
