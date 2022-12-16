var minSetSize = function(arr) {
    arr.sort((a,b)=>a-b);
    let half = (arr.length/2);
    let res = [];
    let count = 1;
    for(let i = 1; i < arr.length; i++) {
        if(arr[i] === arr[i-1]) count++
        else {
            res.push(count);
            count = 1;
        }
    }
    res.push(count);
res.sort((a,b)=>b-a);
let sum = 0;
let index=0;

while(sum<half){
    sum+=res[index]
   index++
    }




return index

};
