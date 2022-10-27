var topKFrequent = function(nums, k) {
    


let res = {};
let a = [];
let p =[];
nums.forEach(element=>{
  if(res[element]){
    res[element]++
  }
  else {
    res[element]=1;
  }
})
let sorted = Object.entries(res).sort((a,b)=>b[1]-a[1])
for(let i = 0 ; i<sorted.length;i++){
 a.push(sorted[i])
 if(a.length==k)break;
}

   
    a.forEach(function (object) {
  var key = Object.keys(a)[0];
  p.push(Number(object[key]))
});;

return p;

};
