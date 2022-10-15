var dailyTemperatures = function(temperatures) {
    let answer = [];
    let count = 0 ;
    for(let i = 0 ; i<temperatures.length; i++){
        var found =false;
for(let j = i+1 ; j<temperatures.length ; j++){
count++;
    
    if(temperatures[j]>temperatures[i]){
found = true;
break;
    
    }
 

}
           if(!found){
           count = 0 ;
                }
        answer.push(count);
        count = 0;
        

    
    }
    return answer;
};
