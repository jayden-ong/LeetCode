/**
 * @param {number[]} nums
 * @return {boolean}
 */
var divideArray = function(nums) {
    let nums_dictionary = {}
    for(num of nums){
        if(num in nums_dictionary){
            nums_dictionary[num] += 1
        }else{
            nums_dictionary[num] = 1
        }
    }

    for(num in nums_dictionary){
        if(nums_dictionary[num] % 2 == 1){
            return false
        }
    }
    return true
};