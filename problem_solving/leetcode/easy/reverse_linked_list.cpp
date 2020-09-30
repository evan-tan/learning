#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 * Input: 1->2->3->4->5->NULL
 * Output: 5->4->3->2->1->NULL
 */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *current  = head;
        ListNode *previous = NULL;
        while (current != NULL)
        {
            ListNode *nextTemp = current->next;
            current->next      = previous;
            previous           = current;
            // Traverse head by 1 position
            current = nextTemp;
        }
        return previous;
    }
};