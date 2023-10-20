/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
 const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => Math.trunc(a / b)
      };
    
      const stack = [];
    
      for (let i of tokens) {
        if (operations[i] != null) {
          const b = stack.pop();
          const a = stack.pop();
          stack.push(operations[i](a, b));
        } else {
          stack.push(Number(i));
        }
      }
    
      return stack[0];
};