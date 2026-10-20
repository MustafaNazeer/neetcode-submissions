/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
if(head == nullptr){
    return nullptr;
}

ListNode* currentPtr = head;
ListNode* previousPtr = nullptr;
ListNode* temp;

while(currentPtr != nullptr){
    temp = currentPtr->next;
    currentPtr->next = previousPtr;
    previousPtr = currentPtr;
    currentPtr = temp;
}
return previousPtr;

    }
};
