var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0]);
  const res = [];
  for(let interval of intervals) {
      const prev = res.at(-1);//index starts at the back
      if (!res.length || prev[1] < interval[0]) {
          res.push(interval);
      } else {
          prev[1] = Math.max(prev[1], interval[1])
      }

  }
  return res;
};
