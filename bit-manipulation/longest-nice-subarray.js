/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function(nums) {
    let left = 0
    let curr = 0
    let answer = 1
    let curr_answer = 0
    for(let right = 0;right < nums.length;right++){
        if((curr & nums[right]) == 0){
            curr_answer += 1
            curr |= nums[right]
        }else{
            answer = Math.max(answer, curr_answer)
            while((curr & nums[right]) != 0){
                curr ^= nums[left]
                left += 1
            }

            curr_answer = right - left + 1
            curr |= nums[right]
        }
    }

    return Math.max(answer, curr_answer)
};