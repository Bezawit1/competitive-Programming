var reverseParentheses = function(s) {
 const stack = [];
  for (let char of s) {
    if (char !== ")") {
      stack.push(char);
      continue;
    }
    let end = stack.pop();
    let answer= [];
    while (end !== "(") {
      answer.push(end);
      end= stack.pop();
    }
    while (answer.length) {
      stack.push(answer.shift());
    }
  }
  return stack.join("");
    
};
