var isValid = function(s) {
    let stack = []

    for (i=0; i < s.length; i++){

        let bracket= s[i];

        switch(bracket) {
            case '(': stack.push(')');
                break;
            case '[': stack.push(']');
                break;
            case '{': stack.push('}')
                break;
            default:
                
                if (bracket !== stack.pop()) return false;       
        }
    }
    return stack.length === 0;
};
