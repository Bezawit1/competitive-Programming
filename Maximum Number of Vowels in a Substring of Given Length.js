var maxVowels = function(s, k) {
    if(s.length < k){
        return 0
    }
    let start = 0,end = 0
    let count = 0,max=0
    for(let i=0;i<s.length;i++){
       
        if(i - start == k){
            
            max = Math.max(max,count)
            if(s.charAt(start) == 'a' || s.charAt(start) == 'e' || s.charAt(start) == 'i' || s.charAt(start) == 'o' || s.charAt(start) == 'u'){
            count--
            }
            start = start + 1
        }
        
        if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u'){
            count++
        }
        
    }
    return Math.max(count,max)
};
