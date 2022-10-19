var myPow = function(x, n) {
 if(x==1||n==0){
     return 1;
 }
if(n<0)
    {
        return 1 / myPow(x, -n);
    }
   
    if(n === 1)
    {
        return x;
    }
    if(n % 2 ===0)
    {
        var product = myPow(x, n/2);
        return product*product;
    }
    else 
    {
         var product = myPow(x, (n-1)/2);
         return product * product * x;
    }
    
    
return x*myPow(x,n-1)
   
};
