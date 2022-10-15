var compress = function(chars) {
 if (chars.length > 1) {
        var str = "";
        let count = 1;
        for (let i = 0; i < chars.length; i++) {
            if (chars[i] === chars[i + 1]){
                count++;
            } else {
                str += chars[i];
                if (count > 1) {
                    str += count;
                   count = 1;
                }
            }
        }

        chars.splice(0, chars.length);

        for (let j = 0; j < str.length; j++) {
            chars[j] = str[j];
        }
    }
    
    return chars.length;
};
