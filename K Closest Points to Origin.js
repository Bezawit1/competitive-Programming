var kClosest = function(points, k) {

  var distance =[];
  var dist=[]
  for(let i of points){
  let x =i[0], y = i[1];
  distance.push(x*x+y*y);
  dist.push([x,y])
      }
      var count = 1;
      var m = []
      distance.sort((a,b)=>a-b)
      while(count<=k){
      for(let j = 0 ; j <dist.length;j++){
        let x =dist[j][0], y = dist[j][1];
        if(x*x+y*y==distance[0]){
      m.push(([x,y]))  
     
          
        }
       
      }
      if(m.length==k)break;
      distance.shift()
      count++;
      }
      
     return m;
    
};
