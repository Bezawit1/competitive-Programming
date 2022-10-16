var lengthOfLongestSubstring = function(s) {
  let start = 0;
  let count = 0;
  const res = {};
  for (let i = 0; i < s.length; i++) {
  
    if (s.charAt(i)in res) {
      start = Math.max(start, res[s.charAt(i)] + 1);
    }
    res[s.charAt(i)] = i;
    count = Math.max(count, i - start + 1);
  }
  return count;
};
