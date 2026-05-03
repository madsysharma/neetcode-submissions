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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* proxy = new ListNode(0, head);
        ListNode* l = proxy;
        ListNode* r = head;

        while(n > 0)
        {
            r = r->next;
            n -= 1;
        }
        while(r != nullptr)
        {
            l = l->next;
            r = r->next;
        }
        l->next = l->next->next;
        return proxy->next;
    }
};
