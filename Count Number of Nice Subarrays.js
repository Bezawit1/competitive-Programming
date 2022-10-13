 const odds = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 == 1 ? 1 : 0) odds.push(i);
  }
  let count = 0;
  for (let i = 0; i < odds.length; i++) {
    const idx = i + k - 1;
    if (idx < odds.length) {
      const start = odds[i - 1] === undefined ? 0 : odds[i - 1] + 1;
      const end = odds[idx + 1] !== undefined ? odds[idx + 1] - 1 : nums.length - 1;
      count = count + (odds[i] - start + 1)*(end - odds[idx] + 1);
    }
    else break;
  }
  return count;
    
};
