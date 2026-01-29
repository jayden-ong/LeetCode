/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */

var determineZero = function(nums) {
    for(let num of nums){
        if(num > 0){
            return false;
        }
    }
    return true
};

var determineSolvable = function(nums, queries, last_queries_index){
    var alterations = []
    for(num of nums){
        alterations.push(0)
    }

    for(let i = 0;i < last_queries_index;i++){
        let left = queries[i][0]
        let right = queries[i][1]
        let val = queries[i][2]
        alterations[left] -= val
        if(right < nums.length - 1){
            alterations[right + 1] += val 
        }
    }

    let curr = 0
    for(let i = 0;i < nums.length;i++){
        curr += alterations[i]
        if(nums[i] + curr > 0){
            return false
        }
    }
    return true
};

var minZeroArray = function(nums, queries) {
    if(determineZero(nums)){
        return 0
    }
    
    if(!determineSolvable(nums, queries, queries.length)){
        return -1
    }
    
    let left = 0
    let right = queries.length - 1
    while(left < right){
        let mid = Math.floor((left + right) / 2)
        if(determineSolvable(nums, queries, mid + 1)){
            right = mid
        }else{
            left = mid + 1
        }
    }
    return left + 1
};