
var MinStack = function() {
    this.myStack = [];
    this.minStack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
  if (
        this.minStack.length === 0 || 
        val <= this.minStack[this.minStack.length - 1]
    ){
        this.minStack.push(val);
    };
    this.myStack.push(val);
   
   
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
     if (this.myStack.pop() === this.minStack[this.minStack.length - 1]){
        this.minStack.pop()
    }
  

};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.myStack[this.myStack.length -1];

};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return this.minStack[this.minStack.length - 1]
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
