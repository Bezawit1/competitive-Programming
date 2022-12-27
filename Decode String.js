var decodeString = function(s) {
   let stack = [];
    let numbers = [];
    let string = [];
    for (let i=0; i<s.length; i++){
        if (!isNaN(Number(s[i]))) {
            stack.push(s[i]);
           
        }
        else{
          
            if (stack.length>0){
                numbers.push(stack.join(""));
                stack=[];
               
            }
          
            if (s[i].match(/\]/)){
                let tempStr = '';
                let current=string.pop();
                while(!current.match(/\[/)){
                    tempStr = current+tempStr;
                    current=string.pop();
                    
                }

                let temp = Number(numbers.pop());
              
                while(temp>0){
                    string.push(tempStr);
                    temp--;
                }
            }else{
                string.push(s[i]);
                
            }
            
        }
    }
    return string.join('')
};
