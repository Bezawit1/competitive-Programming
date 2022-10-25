var findOriginalArray = function(changed) {
let res=[];
    if(changed.length<2 || changed.length%2===1){
        return res;
    }
    changed.sort(function(a,b){return a-b});
    let freq=[];
    for(let i=changed.length-1;i>=0;i--){
        if(freq[changed[i]]===undefined){
            freq[changed[i]] = 1;
        }else{
            freq[changed[i]]++;
        }
    }
    for(let i=changed.length-1;i>=0;i--){
        let j = changed[i];
        if(freq[j]===0){
            continue;
        }
        if(freq[j/2]>0){
            freq[j]--;
            freq[j/2]--;
           
            res.push(j/2);
        }else{
            return [];
        }
    }
    return res;



};
