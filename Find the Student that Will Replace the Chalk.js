var chalkReplacer = function(chalk, k) {
var  i = 0;
    while(i<=chalk.length){
        if(i === chalk.length){
            i = 0;
        } else if(k >= chalk[i]){
            k -= chalk[i];
            i++;
        } else {
            return i;
        }
    }
            
    
   

};
