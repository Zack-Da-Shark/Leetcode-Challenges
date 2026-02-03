/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        int addition = l1.val + l2.val;
        int carryAmount = 0;
        while(addition >= 10)
        {
            carryAmount++;
            addition -= 10;
        }
        //First node is done
        ListNode result = new ListNode(addition);
        result.next = addNodes(l1.next, l2.next, carryAmount);
        return result;
    }

    
    public ListNode addNodes(ListNode l1, ListNode l2, int carryAmount)
    {
        int addition = 0;
        ListNode result = new ListNode();
        if(l1 == null && l2 == null)
        {
            if(carryAmount != 0)
            {
                result.val = carryAmount;
                return result;
            }
            return null;
        }
        else if(l1 == null)
        {
            addition = l2.val + carryAmount;
            carryAmount = 0;
            while(addition >= 10)
            {
                carryAmount++;
                addition -= 10;
            }
            result.val = addition;
            result.next = addNodes(l1, l2.next, carryAmount);
        }
        else if(l2 == null)
        {
            addition = l1.val + carryAmount;
            carryAmount = 0;
            while(addition >= 10)
            {
                carryAmount++;
                addition -= 10;
            }
            result.val = addition;
            result.next = addNodes(l1.next, l2, carryAmount);
        }
        else
        {   
            addition = l1.val + l2.val + carryAmount;
            carryAmount = 0;
            while(addition >= 10)
            {
                carryAmount++;
                addition -= 10;
            }
            result.val = addition;
            result.next = addNodes(l1.next, l2.next, carryAmount);
        }
        return result;
    }
}

//This is a recursive solution
//risky due to stack overflow potential
//can fix overflow by iteration but more complex, trust me, I've tried and almost committed great violence against my device