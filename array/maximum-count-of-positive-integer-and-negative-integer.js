/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    let num_positive = 0
    let num_negative = 0
    for(let i of nums){
        if(i < 0){
            num_negative = num_negative + 1
        }else if(i > 0){
            num_positive = num_positive + 1
        }
    }

    if(num_negative > num_positive){
        return num_negative
    } 
    return num_positive
};