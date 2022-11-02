function TH(n,m,a){

let count1 = parseInt (m/a);
let count2 = parseInt( n/a);
 if(n%a !== 0)
            ++count2;
            
        if(m%a !== 0)
            ++count1;
            
            
            return count1*count2
}
