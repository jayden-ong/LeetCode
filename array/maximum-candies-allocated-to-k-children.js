/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var validateCandies = function(candies, k, desired_candies) {
    let num_children = k
    for(candy of candies){
        num_children -= Math.floor(candy / desired_candies)
        if(num_children <= 0) {
            return true
        }
    }
    return false
}

var maximumCandies = function(candies, k) {
    let left = 0
    let right = 0
    for(candy of candies){
        right += candy
    }
    right = Math.floor(right / k)
    while(left <= right){
        mid = Math.floor((left + right) / 2)
        if(validateCandies(candies, k, mid)){
            left = mid + 1
        }else{
            right = mid - 1
        }
    }
    return left - 1
};