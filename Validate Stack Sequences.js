var validateStackSequences = function(pushed, popped) {
  let arr1 = []
    let i = 0

    for (let j of pushed) {
        arr1.push(j)
        while (arr1.length && arr1[arr1.length - 1] === popped[i]) {
            arr1.pop()
            i++
        }
    }
    
    return pushed.length === i



};
