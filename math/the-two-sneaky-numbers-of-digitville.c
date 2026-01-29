/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
    // Our answer is going to contain two ints
    *returnSize = 2;
    int* answer = (int *)malloc(sizeof(int) * 2);
    int index = 0;
    int table[101];
    for(int i = 0;i < numsSize;i++){
        table[nums[i]] += 1;
        if(table[nums[i]] >= 2){
            answer[index] = nums[i];
            index += 1;
        }
    }
    return answer;
}