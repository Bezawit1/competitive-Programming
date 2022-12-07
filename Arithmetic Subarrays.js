var checkArithmeticSubarrays = function(nums, l, r) {
  let answer=[]
 
for(let i = 0 ;i<l.length;i++){
  let k = 0
 let res =[]

  let ele = r[i]-l[i]+1
for(let j=l[i];j<=r[i];j++){
 res[k++] = nums[j]
  
}
res.sort((a,b)=>a-b)
let diff = res[1] -res[0]
let boolean =true
for(let j=1;j<ele-1;j++){
 if(diff!=res[j+1]-res[j]){
 boolean = false
break
 }
 
}
answer.push(boolean)

}
return answer
}
