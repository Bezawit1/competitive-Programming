
var MyQueue = function() {
    this.myQueue =[]
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
   this.myQueue.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
    if(this.myQueue.length>0){
   return this.myQueue.shift();

}
    return false;
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
   if(this.myQueue.length>0){
return this.myQueue[0];
   
   }
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
   return this.myQueue.length === 0;
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
