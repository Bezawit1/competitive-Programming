var removeKdigits = function(num, k) {

    if(num.length===k) return '0';
    
    let res=[];
    num.split('')
	
    for(let i = 0 ;i<num.length;i++){
		
        while(res.length!==0 && res[res.length-1]>num[i] && k>0){
			
            res.pop();
         
			k--;
        }
            res.push(+num[i]);
     
        
    }
   
    while(res[0]===0&&res.length>1){
        res.shift();
    }


    while(k--){
        res.pop();
    }
  
    return res.length ? res.join('') : '0'   
};
