/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCapability = function(nums, k) {
    smallest = nums[0]
    largest = nums[0]
    for(num of nums){
        if(num < smallest){
            smallest = num
        }

        if(num > largest){
            largest = num
        }
    }

    while(smallest < largest){
        mid = Math.floor((smallest + largest) / 2)
        curr_index = 0
        num_houses = k
        while(curr_index < nums.length){
            if(nums[curr_index] <= mid){
                num_houses -= 1
                curr_index += 1
            }
            curr_index += 1
        }

        if(num_houses <= 0){
            largest = mid
        }else{
            smallest = mid + 1
        }
    }

    return largest
};