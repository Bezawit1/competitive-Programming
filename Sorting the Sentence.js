var sortSentence = function(s) {
    
  let sorted = [];
  for (let i of s.split(' ')) {
    let index = i[i.length - 1] - 1;
    sorted[index] = i.slice(0, i.length - 1);
  }
  return sorted.join(" ");
};
