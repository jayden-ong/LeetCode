/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    // Want to figure out in constant time if the current value is a node
    int* nums_used = (int*)calloc(100001, sizeof(int));
    for(int i = 0;i < numsSize;i++){
        nums_used[nums[i]] += 1;
        printf("%d", nums_used[nums[i]]);
    }

    struct ListNode* curr = head;
    // We first need to figure out what the head of our answer is
    while(nums_used[curr->val] > 0){
        curr = curr->next;
    }
    // We now know the head of our answer
    struct ListNode* answer = curr;
    // We keep going until there are no more nodes
    while(curr->next != NULL){
        // It appears, get rid of it
        if(nums_used[curr->next->val] > 0){
            // We know that curr->next will not be NULL because of the while condition
            curr->next = curr->next->next;
        }else{
            curr = curr->next;
        }
    }
    free(nums_used);
    return answer;
}