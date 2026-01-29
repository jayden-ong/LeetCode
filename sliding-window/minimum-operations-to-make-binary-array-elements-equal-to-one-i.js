/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let answer = 0
    for(let i = 0;i < nums.length;i++){
        if(nums[i] == 0){
            if(i + 2 < nums.length){
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                answer += 1
            } else {
                return -1
            }
        }
    }
    return answer
};