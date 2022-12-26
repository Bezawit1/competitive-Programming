var calculate = function(s) {
const stack = [];
    
    let last_operator = '+'
    let current_number = 0;
    
    for(let i = 0; i <= s.length; ++i){
        const element = s[i];
        
        if(i === s.length|| operations(element)){ 
            if(last_operator === '*'){
                const num = stack.pop(); 
                stack.push(num * current_number);
            }else if(last_operator === '/'){
                const num = stack.pop(); 
                stack.push(Math.trunc(num / current_number));
            } else if(last_operator === '+'){
                stack.push(current_number);
            } else if(last_operator === '-'){
                stack.push(-1 * current_number);
            }
            current_number = 0;
            last_operator = element;
        }else if(is_digit(element)){ 
            current_number = (current_number * 10) + Number(element);
        }
    }
    
    return stack.reduce((acc, el)=>acc+el);
};



function operations(operation){
    return operation=== '+' || operation === '-' || operation=== '*' || operation === '/'
}

function is_digit(element){
    return '0' <= element && element <= '9';
};
