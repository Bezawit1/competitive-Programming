function gradingStudents(grades) {
    // Write your code here

     let res = [];
        for(let i = 0; i < grades.length; i++) {
            if(grades[i] < 38 || grades[i] % 5 == 0) {
                res.push(grades[i])
            } else if(grades[i] % 5 != 0) {
               let difference = (parseInt(grades[i] / 5) + 1) * 5 - grades[i];
               
               if(difference < 3) {
                   res.push((parseInt(grades[i] / 5) + 1) * 5);
                } else {
                    res.push(grades[i]);
                }
            }  
        }
        return res;
}
